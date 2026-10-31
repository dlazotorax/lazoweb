from rdkit import Chem
from rdkit.Chem import AllChem, rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image, ImageFilter, ImageDraw, ImageChops
import io
smi='CC1(C)C(/C=C/C=C/C=C/C=C2/N(CCCCS(=O)(=O)[O-])c3ccc4ccccc4c3C2(C)C)=[N+](CCCCS(=O)(=O)[O-])c2ccc3ccccc3c21'
m=Chem.MolFromSmiles(smi)
rdDepictor.SetPreferCoordGen(True); rdDepictor.Compute2DCoords(m)
def render(w,h,col,lw):
    d=rdMolDraw2D.MolDraw2DCairo(w,h)
    o=d.drawOptions(); o.clearBackground=False; o.setBackgroundColour((0,0,0,0))
    o.setAtomPalette({-1:col}); o.bondLineWidth=lw; o.padding=0.04; o.minFontSize=34; o.maxFontSize=46
    o.annotationFontScale=0.6
    d.DrawMolecule(m); d.FinishDrawing()
    return Image.open(io.BytesIO(d.GetDrawingText())).convert('RGBA')
BG=(28,31,36)
src=Image.open('/root/.claude/uploads/e55b536e-37f1-56ee-ac55-81eed06452f0/98039b72-image.jpg').convert('RGB')
im=src.copy(); dr=ImageDraw.Draw(im)
def clear(box,f=(40,20,40,20)):
    x0,y0,x1,y1=box; fl,ft,fr,fb=f
    patch=Image.new('RGB',(x1-x0,y1-y0),BG)
    W,H=patch.size
    mask=Image.new('L',(W,H),0); px=mask.load()
    for x in range(W):
        for y in range(H):
            v=1.0
            if fl and x<fl: v=min(v,x/fl)
            if fr and x>W-1-fr: v=min(v,(W-1-x)/fr)
            if ft and y<ft: v=min(v,y/ft)
            if fb and y>H-1-fb: v=min(v,(H-1-y)/fb)
            px[x,y]=int(255*v)
    im.paste(patch,(x0,y0),mask)
def place(box,glow,col,lw,alpha=1.0):
    global im
    x0,y0,x1,y1=box; W,H=x1-x0,y1-y0
    mol=render(W*2,H*2,col,lw*2).resize((W,H),Image.LANCZOS)
    mol.putalpha(mol.getchannel('A').point(lambda a:0 if a<24 else a))
    layer=Image.new('RGBA',im.size,(0,0,0,0)); layer.paste(mol,(x0,y0))
    A_=layer.getchannel('A')
    base=im.convert('RGBA')
    for blur,mult,c in [(glow,2.0,(80,255,110)),(glow*4,1.3,(60,220,90))]:
        g=Image.new('RGBA',im.size,c+(0,)); g.putalpha(A_.filter(ImageFilter.GaussianBlur(blur)).point(lambda a,m=mult:min(255,int(a*m)))); base=Image.alpha_composite(base,g)
    im=Image.alpha_composite(base,layer).convert('RGB')
keep=src.crop((1700,948,2100,1030))
x0,y0,x1,y1=960,522,2205,1100
patch=Image.new('RGB',(x1-x0,y1-y0),BG); W,H=patch.size
mask=Image.new('L',(W,H),255); md=ImageDraw.Draw(mask)
for i in range(80): md.line([(i,0),(i,H)],fill=int(255*i/80))
im.paste(patch,(x0,y0),mask)
im.paste(keep,(1700,948))
dr=ImageDraw.Draw(im)
# sound waves toward the camera
wl=Image.new('RGBA',im.size,(0,0,0,0)); wd=ImageDraw.Draw(wl)
cx,cy=2100,757
for rr in (38,66,94):
    wd.arc([cx-rr,cy-rr,cx+rr,cy+rr],-38,38,fill=(90,230,110,255),width=8)
glow=Image.new('RGBA',im.size,(70,230,100,0)); glow.putalpha(wl.getchannel('A').filter(ImageFilter.GaussianBlur(8)).point(lambda a:min(255,int(a*1.5))))
base=im.convert('RGBA'); base=Image.alpha_composite(base,glow); base=Image.alpha_composite(base,wl); im=base.convert('RGB'); dr=ImageDraw.Draw(im)
A=(1040,545,1570,985); F=(1560,535,2030,930)
place(A,1.5,(0.28,0.72,0.36),4,1.0)
place(F,9,(0.60,1.0,0.65),5)
out=im.crop((0,0,im.width,1100)); out.save('icg/fen2_full.png')
o2=out.copy(); o2.thumbnail((1200,1200)); o2.save('icg/icg-fenomeno.webp',quality=88); o2.save('icg/fen2.png'); print(o2.size)
