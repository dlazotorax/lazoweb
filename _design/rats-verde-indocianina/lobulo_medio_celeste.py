import numpy as np, cv2
from PIL import Image
im=np.array(Image.open('seg/fixed.png').convert('RGB')).astype(float)
g=cv2.cvtColor(im.astype(np.uint8),cv2.COLOR_RGB2GRAY).astype(int)
H,W=g.shape
# oblique fissure x per row
pred=lambda y: 493+(y-950)*(771-493)/(1443-950)
obl={}
for y in range(945,1460):
    xs=[x for x in range(int(pred(y))-45,int(pred(y))+45) if g[y,x]<110]
    if xs: obl[y]=int(np.median(xs))
ys=sorted(obl); 
# smooth/interpolate
yy=np.arange(940,1480); ox=np.interp(yy,ys,[obl[y] for y in ys])
ox=np.convolve(np.pad(ox,7,mode='edge'),np.ones(15)/15,'valid')
# horizontal fissure y per column
hz={}
for x in range(480,980):
    exp=955+(x-500)*(1080-955)/(950-500)
    c=[y for y in range(int(exp)-40,int(exp)+40) if g[y,x]<110]
    if c: hz[x]=int(np.median(c))
xs=sorted(hz); xx=np.arange(450,1000); hy=np.interp(xx,xs,[hz[x] for x in xs])
hy=np.convolve(np.pad(hy,7,mode='edge'),np.ones(15)/15,'valid')
lung=(im.sum(2)<735)
mask=np.zeros((H,W),bool)
for y in range(930,1480):
    for x in range(450,1000):
        if not lung[y,x]: continue
        if x>ox[min(max(y-940,0),len(ox)-1)]+4 and y>hy[x-450]+4: mask[y,x]=True
# keep only largest component
n,lab,st,_=cv2.connectedComponentsWithStats(mask.astype(np.uint8))
k=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); mask=lab==k
# exclude dark outline/leader-line pixels from recolor
keep=g<70
m=mask&~keep
L=g.astype(float); mu=L[m].mean(); sd=L[m].std()
t=np.clip(0.55+(L-mu)/(4*sd),0,1)
dark=np.array([72,150,205.]); light=np.array([180,224,247.])
new=dark[None,None,:]*(1-t[...,None])+light[None,None,:]*t[...,None]
# soften edge
mf=cv2.GaussianBlur(m.astype(float),(5,5),0)[...,None]
out=im*(1-mf)+new*mf
Image.fromarray(out.clip(0,255).astype(np.uint8)).save('seg/fixed_blue.png')
print(m.sum(), mu, sd)
