from PIL import Image, ImageDraw, ImageFont
R=Image.open('right_lobes.png'); L=Image.open('left_lobes.png')
W,H=1200,800; OY=120
c=Image.new('RGBA',(W,H),(255,255,255,255)); c.alpha_composite(R,(0,OY)); c.alpha_composite(L,(600,OY))
d=ImageDraw.Draw(c)
FB=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',44)
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',23)
for x,t in [(300,'PULMÓN DERECHO'),(900,'PULMÓN IZQUIERDO')]:
    w=d.textlength(t,font=FB); d.text((x-w/2,40),t,font=FB,fill=(0,0,0))
def lab(txt,tx,ty,l0,l1,ly,align):
    d.line([(l0,ly+OY),(l1,ly+OY)],fill=(0,0,0),width=2)
    d.multiline_text((tx,ty+OY),txt,font=F,fill=(0,0,0),align=align,spacing=4)
d.arc((600+92-52,OY+338-58,600+92+52,OY+338+58),start=-40,end=58,fill=(150,96,104),width=3)
# right lung
lab('Lóbulo\nsuperior',38,103,140,230,140,'right')
lab('Lóbulo\nmedio',500,402,425,492,428,'left')
lab('Lóbulo\ninferior',8,430,104,175,455,'right')
# left lung (mirrored)
lab('Lóbulo\nsuperior',1068,103,970,1060,140,'left')
lab('Língula',612,416,722,776,428,'left')
lab('Lóbulo\ninferior',1106,430,1025,1098,455,'left')
c.convert('RGB').save('pulmones-lobulos.png'); c.convert('RGB').save('/home/claude/work/repo/dist/rats/resecciones/imgs/pulmones-lobulos.webp',quality=88)
c.convert('RGB').resize((900,600)).save('pl.jpg')
