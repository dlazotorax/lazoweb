import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
SRC='/root/.claude/uploads/e55b536e-37f1-56ee-ac55-81eed06452f0/582d612c-image.jpg'
im=np.array(Image.open(SRC).convert('RGB'))
gray=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
REG='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
BOLD='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def bbox_dark(x0,y0,x1,y1,thr=110):
    r=gray[y0:y1,x0:x1]<thr; ys,xs=np.where(r)
    return (xs.min()+x0,ys.min()+y0,xs.max()+x0,ys.max()+y0)
# ---- 1) inpaint leader lines inside the lungs
mask=np.zeros(gray.shape,np.uint8)
def seg(p,q,w=13): cv2.line(mask,p,q,255,w)
seg((2040,791),(2195,791),15)          # Lateral S4 (right) - remove
seg((1935,931),(2195,931))          # Medial S5 (right) - remove
seg((2040,1357),(2180,1447))        # Basal lateral S9 (right) - remove
seg((1400,1041),(1566,1041))        # Superior S6 (left) - remove
seg((1456,1388),(1562,1345))        # Basal posterior S10 - inner part
seg((626,1137),(842,1137),19)          # Cisura oblicua line, inner part (left drawing)
# refine: only dark pixels of the lines (plus 2px) to keep texture
im=cv2.inpaint(im,mask,6,cv2.INPAINT_TELEA)
src0=np.array(Image.open(SRC).convert('RGB'))
for yc in (791,931):
    for y in range(yc-9,yc+10):
        im[y,2128:2165]=src0[y-14 if y<yc else y+14,2128:2165]
P=Image.fromarray(im); d=ImageDraw.Draw(P)
W=(255,255,255)
def white(b,pad=6): d.rectangle((b[0]-pad,b[1]-pad,b[2]+pad,b[3]+pad),fill=W)
# ---- 2) remove old texts (right side x>=2190, left side x<=1412, bottom)
boxes={
 'latR':(2190,750,2400,880),'medR':(2190,890,2400,1020),'supR':(2190,1065,2400,1190),
 'basantR':(2190,1210,2400,1390),'baslatR':(2185,1400,2400,1575),
 'bottom':(1560,1480,2010,1560),
 'latL':(1240,825,1412,955),'supL':(1215,1000,1410,1120),'basmedL':(1240,1150,1405,1335),
 'cis':(990,1095,1180,1230),
}
orig={k:bbox_dark(*v) for k,v in boxes.items()}
for k,b in orig.items(): white(b)
# stray leftover of right lines outside lung (x 2156..2195)
d.rectangle((2160,785,2195,797),fill=W); d.rectangle((2160,924,2195,936),fill=W)
d.line([(2150,1420),(2195,1450)],fill=W,width=12)
F2=ImageFont.truetype(REG,94); LH=56
TXT=Image.new('L',(P.size[0]*2,P.size[1]*2),0); td=ImageDraw.Draw(TXT)
def label(lines,cx,cy):
    tot=LH*len(lines); y=cy-tot/2
    for t in lines:
        w=td.textlength(t,font=F2)/2; td.text(((cx-w/2)*2,y*2),t,font=F2,fill=255,stroke_width=1,stroke_fill=255); y+=LH
def ctr(b): return ((b[0]+b[2])/2,(b[1]+b[3])/2)
label(['Lateral','(S4)'],*ctr(orig['supR']))
label(['Medial','(S5)'],*ctr(orig['basantR']))
cx,cy=ctr(orig['bottom']); label(['Basal anterior (S8)'],cx,cy+4)
label(['Superior','(S6)'],*ctr(orig['latL']))
label(['Basal','lateral','(S9)'],*ctr(orig['basmedL']))
label(['Lóbulo','medio'],*ctr(orig['cis']))
A=TXT.resize(P.size,Image.LANCZOS); P.paste((0,0,0),(0,0),A); d=ImageDraw.Draw(P)
# retargeted S10 leader end
d.line([(1400,1410),(1452,1390)],fill=(0,0,0),width=4)
# ---- 3) titles
tL=bbox_dark(250,40,1000,260); tR=bbox_dark(1250,40,2390,260)
white(tL,10); white(tR,10)
FB=ImageFont.truetype(BOLD,104)
for t,b in [('LÓBULOS',tL),('SEGMENTOS',tR)]:
    cx=(b[0]+b[2])/2; w=d.textlength(t,font=FB); bb=FB.getbbox(t)
    y=(b[1]+b[3])/2-(bb[1]+bb[3])/2
    d.text((cx-w/2,y),t,font=FB,fill=(0,0,0))
P.save('seg/fixed.png'); print(orig)
