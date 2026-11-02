import numpy as np, trimesh
from skimage import measure
H=24.0
def _lf(X,Y,Z):
    t=np.clip(Z/H,0,1)
    om=np.clip(1-t,0,1)
    xp=0.4-9.4*np.clip(1-t**2.0,0,1)**0.5
    xa=0.4+7.6*np.clip(1-t**2.6,0,1)**0.55
    a=(xa-xp)/2+0.02; cx=(xa+xp)/2
    u=(X-cx)/a
    up=np.clip(u,-1.2,1.2)
    T=(5.4*np.clip((1-up)/2,0,None)**0.7+0.5)*(np.clip(1-t**3,0,1)**0.35+0.1)
    v=np.where(Y<0,Y/T,Y/(0.72*T))
    p=2.2
    fs=(np.abs(u)**p+np.abs(v)**p)**(1/p)-1.0+0.025*noise3(X,Y,Z,7,0.45)
    zb=0.9+0.13*X+2.6*np.exp(-((X-0.8)/4.6)**2-(Y/4.0)**2)
    fb=(zb-Z)/3.0
    fa=(Z-(H+0.3))/3.0
    return np.maximum(fs,np.maximum(fb,fa))
def zo(X): return 14.0-(X+8.5)*(13.0/14.0)
SO=13.0/14.0
def d_obl(X,Z): return (Z-zo(X))/np.sqrt(1+SO**2)+0.35*np.sin(0.7*X+1.3)*np.sin(0.45*Z)
ZH=9.6
def d_hor(X,Z): return Z-(ZH+0.06*X)+0.3*np.sin(0.8*X+0.4)
def lobe(X,Y,Z,name,g=0.13):
    do=d_obl(X,Z); dh=d_hor(X,Z)
    if name=='lower': return np.minimum(-do-g, 9)
    if name=='upper': return np.minimum(do-g,dh-g)
    if name=='middle': return np.minimum(do-g,-dh-g)
def noise3(X,Y,Z,seed=0,sc=1.3):
    r=np.random.RandomState(seed); s=0
    for k in range(4):
        f=r.uniform(0.6,1.4,3)*sc*(1.7**k)
        ph=r.uniform(0,6.28,3)
        s+=np.sin(f[0]*X+ph[0])*np.sin(f[1]*Y+ph[1])*np.sin(f[2]*Z+ph[2])/(1.8**k)
    return s
def mesh_from(F,grid,smooth=12):
    xs,ys,zs=grid
    sp=(xs[1]-xs[0],ys[1]-ys[0],zs[1]-zs[0])
    from scipy.ndimage import gaussian_filter
    F=gaussian_filter(F,1.3)
    v,fc,n,_=measure.marching_cubes(F,0.0,spacing=sp)
    v+=np.array([xs[0],ys[0],zs[0]])
    m=trimesh.Trimesh(v,fc[:,::-1],process=True)
    trimesh.smoothing.filter_taubin(m,iterations=smooth)
    return m

lung_field=_lf
