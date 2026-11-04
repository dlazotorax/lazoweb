import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
src=np.array(Image.open('lobL.png').convert('RGB')).astype(np.uint8)
hsv=cv2.cvtColor(src,cv2.COLOR_RGB2HSV)
sat=hsv[...,1].astype(int); val=hsv[...,2].astype(int)
col=(sat>40)&(val>60)
col=ndi.binary_opening(col,iterations=1)
lab,n=ndi.label(col); sizes=ndi.sum(col,lab,range(1,n+1)); big=lab==(np.argmax(sizes)+1)
lung=ndi.binary_fill_holes(ndi.binary_closing(big,iterations=4))
lung=ndi.binary_erosion(lung,iterations=1)
# dark line pixels inside lung -> inpaint
lungD=ndi.binary_dilation(lung,iterations=3)
dark=((val<100)&lungD)
dark=ndi.binary_dilation(dark,iterations=3)&lungD
clean=cv2.inpaint(src,(dark*255).astype(np.uint8),5,cv2.INPAINT_TELEA)
# keep the lung outline: re-dilate mask by 1 to keep border pixels
lung2=ndi.binary_dilation(lung,iterations=2)
rgba=np.dstack([clean,(lung2*255).astype(np.uint8)])
R=Image.fromarray(rgba,'RGBA'); R.save('right_lobes.png')
# left lung: mirror and recolor blue->yellow
L=clean[:,::-1].copy(); Lm=lung2[:,::-1]
h2=cv2.cvtColor(L,cv2.COLOR_RGB2HSV).astype(float)
blue=(h2[...,0]>85)&(h2[...,0]<130)&(h2[...,1]>50)&Lm
blue=ndi.binary_closing(blue,iterations=3)&Lm
yel=(h2[...,0]>15)&(h2[...,0]<35)&(h2[...,1]>50)&Lm
ym=[h2[...,k][yel].mean() for k in range(3)]; ys=[h2[...,k][yel].std() for k in range(3)]
bm=[h2[...,k][blue].mean() for k in range(3)]; bs=[h2[...,k][blue].std() for k in range(3)]
for k in (1,2):
    h2[...,k][blue]=(h2[...,k][blue]-bm[k])/(bs[k]+1e-6)*ys[k]+ym[k]
h2[...,0][blue]=ym[0]
L2=cv2.cvtColor(np.clip(h2,0,255).astype(np.uint8),cv2.COLOR_HSV2RGB)
# blend boundary yellow/blue (old horizontal fissure) by inpainting a band
band=ndi.binary_dilation(blue,iterations=7)&ndi.binary_dilation(yel,iterations=7)&ndi.binary_erosion(Lm,iterations=6)
L2=cv2.inpaint(L2,(band*255).astype(np.uint8),9,cv2.INPAINT_TELEA)
# cardiac notch on anterior border (left side after mirroring)
H,W=Lm.shape; yy,xx=np.mgrid[0:H,0:W]
ell=((xx-92)/52.0)**2+((yy-338)/58.0)**2<1
Lm=Lm&~ell
edge=Lm&~ndi.binary_erosion(Lm,iterations=2)
notch_edge=edge&(((xx-92)/58.0)**2+((yy-338)/64.0)**2<1)
L2[notch_edge]=(150,96,104)
Image.fromarray(np.dstack([L2,(Lm*255).astype(np.uint8)]),'RGBA').save('left_lobes.png')
print(src.shape, blue.sum(), yel.sum())
