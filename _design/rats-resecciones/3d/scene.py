import sys, numpy as np, trimesh, bpy, math, mathutils
sys.path.insert(0,'.')
from geom import *
MODE=sys.argv[sys.argv.index('--')+1]; OUT=sys.argv[sys.argv.index('--')+2]
RES=float(sys.argv[sys.argv.index('--')+3]) if len(sys.argv)>sys.argv.index('--')+3 else 0.12
SAMPLES=int(sys.argv[sys.argv.index('--')+4]) if len(sys.argv)>sys.argv.index('--')+4 else 48
xs=np.arange(-10,10,RES); ys=np.arange(-7.5,5.5,RES); zs=np.arange(-3,26,RES)
X,Y,Z=np.meshgrid(xs,ys,zs,indexing='ij')
LF=lung_field(X,Y,Z)
g=0.2
def W(X,Y,Z):  # wedge at anterior border of upper lobe
    return np.minimum(X-2.3,(X-2.3)*math.tan(math.radians(24))-np.abs(Z-15.2))
HP=np.array([-1.0,2.0,12.4]); AX=np.array([-0.62,-0.42,0.66]); AX=AX/np.linalg.norm(AX)
def S2(X,Y,Z):
    vx,vy,vz=X-HP[0],Y-HP[1],Z-HP[2]; r=np.sqrt(vx**2+vy**2+vz**2)+1e-6
    proj=vx*AX[0]+vy*AX[1]+vz*AX[2]
    n=0.25*noise3(X,Y,Z,3,0.6)
    return proj-r*math.cos(math.radians(31))+n
NOD=np.array([4.6,-1.75,15.2]); NR=0.6
parts=[]  # (name, field, offset, kind)
LOBOFF=(-0.6,-4.2,7.2)
up=-lobe(X,Y,Z,'upper'); mid=-lobe(X,Y,Z,'middle'); low=-lobe(X,Y,Z,'lower')
if MODE=='cuna':
    w=W(X,Y,Z)
    parts+=[('upper',np.maximum.reduce([LF,up,w+g]),(0,0,0),'keep'),
            ('wedge',np.maximum.reduce([LF,up,-w+g]),(1.7,-1.5,0.3),'res'),
            ('middle',np.maximum(LF,mid),(0,0,0),'keep'),('lower',np.maximum(LF,low),(0,0,0),'keep')]
elif MODE=='seg':
    s=S2(X,Y,Z)
    parts+=[('upper',np.maximum.reduce([LF,up,s+g]),(0,0,0),'keep'),
            ('s2',np.maximum.reduce([LF,up,-s+g]),tuple(AX*4.6),'res'),
            ('middle',np.maximum(LF,mid),(0,0,0),'keep'),('lower',np.maximum(LF,low),(0,0,0),'keep')]
elif MODE=='lob':
    parts+=[('upper',np.maximum(LF,up),LOBOFF,'res'),
            ('middle',np.maximum(LF,mid),(0,0,0),'keep'),('lower',np.maximum(LF,low),(0,0,0),'keep')]
else:
    parts+=[('upper',np.maximum(LF,up),(0,0,0),'keep'),('middle',np.maximum(LF,mid),(0,0,0),'keep'),('lower',np.maximum(LF,low),(0,0,0),'keep')]

bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
def mat_pleura(name,base,edge,dark=False):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree; N=nt.nodes; L=nt.links
    b=N['Principled BSDF']
    tc=N.new('ShaderNodeTexCoord')
    vor=N.new('ShaderNodeTexVoronoi'); vor.feature='DISTANCE_TO_EDGE'; vor.inputs['Scale'].default_value=2.2
    L.new(tc.outputs['Object'],vor.inputs['Vector'])
    noi=N.new('ShaderNodeTexNoise'); noi.inputs['Scale'].default_value=2.5; noi.inputs['Detail'].default_value=8
    L.new(tc.outputs['Object'],noi.inputs['Vector'])
    ramp=N.new('ShaderNodeValToRGB'); ramp.color_ramp.elements[0].position=0.0; ramp.color_ramp.elements[0].color=edge
    ramp.color_ramp.elements[1].position=0.035; ramp.color_ramp.elements[1].color=base
    L.new(vor.outputs['Distance'],ramp.inputs['Fac'])
    mix=N.new('ShaderNodeMix'); mix.data_type='RGBA'; mix.inputs['Factor'].default_value=0.10
    L.new(ramp.outputs['Color'],mix.inputs[6]); L.new(noi.outputs['Color'],mix.inputs[7])
    L.new(mix.outputs[2],b.inputs['Base Color'])
    b.inputs['Roughness'].default_value=0.32
    b.inputs['Subsurface Weight'].default_value=0.25; b.inputs['Subsurface Radius'].default_value=(0.6,0.25,0.2); b.inputs['Subsurface Scale'].default_value=0.4
    b.inputs['Coat Weight'].default_value=0.2; b.inputs['Coat Roughness'].default_value=0.12
    bump=N.new('ShaderNodeBump'); bump.inputs['Strength'].default_value=0.25; bump.inputs['Distance'].default_value=0.05
    add=N.new('ShaderNodeMath'); add.operation='ADD'
    L.new(vor.outputs['Distance'],add.inputs[0]); L.new(noi.outputs['Fac'],add.inputs[1])
    L.new(add.outputs[0],bump.inputs['Height']); L.new(bump.outputs['Normal'],b.inputs['Normal'])
    return m
def mat_cut(name,base):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree; N=nt.nodes; L=nt.links
    b=N['Principled BSDF']; tc=N.new('ShaderNodeTexCoord')
    noi=N.new('ShaderNodeTexNoise'); noi.inputs['Scale'].default_value=9; noi.inputs['Detail'].default_value=10
    L.new(tc.outputs['Object'],noi.inputs['Vector'])
    ramp=N.new('ShaderNodeValToRGB'); ramp.color_ramp.elements[0].color=tuple(c*0.55 for c in base[:3])+(1,); ramp.color_ramp.elements[1].color=base
    L.new(noi.outputs['Fac'],ramp.inputs['Fac']); L.new(ramp.outputs['Color'],b.inputs['Base Color'])
    b.inputs['Roughness'].default_value=0.55; b.inputs['Coat Weight'].default_value=0.15; b.inputs['Coat Roughness'].default_value=0.1
    bump=N.new('ShaderNodeBump'); bump.inputs['Strength'].default_value=0.6; bump.inputs['Distance'].default_value=0.04
    L.new(noi.outputs['Fac'],bump.inputs['Height']); L.new(bump.outputs['Normal'],b.inputs['Normal'])
    return m
def mat_simple(name,col,rough=0.3,metal=0.0):
    m=bpy.data.materials.new(name); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value=col; b.inputs['Roughness'].default_value=rough; b.inputs['Metallic'].default_value=metal
    return m
PLE=mat_pleura('pleura',(0.78,0.36,0.34,1),(0.36,0.25,0.29,1))
PLE_R=mat_pleura('pleura_res',(0.55,0.20,0.27,1),(0.30,0.15,0.2,1))
CUT=mat_cut('cut',(0.50,0.09,0.10,1))
STA=mat_simple('staple',(0.85,0.86,0.88,1),0.25,1.0)
NODM=mat_simple('nodule',(0.82,0.78,0.70,1),0.5)

def add_mesh(name,m,offset,kind):
    c=m.triangles_center
    lf=lung_field(c[:,0],c[:,1],c[:,2])
    do=np.abs(np.abs(d_obl(c[:,0],c[:,2]))-g); dh=np.abs(np.abs(d_hor(c[:,0],c[:,2]))-g)
    ple=(lf>-0.2)|( ((do<0.12)|((dh<0.12)&(d_obl(c[:,0],c[:,2])>0))) & True)
    if MODE=='cuna': ple&=~(np.abs(W(c[:,0],c[:,1],c[:,2]))<0.25)
    if MODE=='seg' and name in('upper','s2'): ple&=~(np.abs(S2(c[:,0],c[:,1],c[:,2]))<0.25)
    me=bpy.data.meshes.new(name); me.from_pydata(m.vertices.tolist(),[],m.faces.tolist()); me.update()
    me.materials.append(PLE_R if kind=='res' else PLE); me.materials.append(CUT)
    mi=np.where(ple,0,1).astype(np.int32); me.polygons.foreach_set('material_index',mi)
    me.polygons.foreach_set('use_smooth',[True]*len(me.polygons))
    ob=bpy.data.objects.new(name,me); sc.collection.objects.link(ob); ob.location=offset
    # staples along cut/pleura boundary
    adj=m.face_adjacency; e=m.face_adjacency_edges
    sel=ple[adj[:,0]]!=ple[adj[:,1]]
    E=e[sel]; P=(m.vertices[E[:,0]]+m.vertices[E[:,1]])/2; D=m.vertices[E[:,1]]-m.vertices[E[:,0]]
    pts=[];dirs=[]
    for p,d in zip(P,D):
        if all(np.linalg.norm(p-q)>0.32 for q in pts[-40:]): pts.append(p); dirs.append(d)
    if pts:
        P2=np.array(pts)
        if MODE=='cuna': keep=np.abs(W(P2[:,0],P2[:,1],P2[:,2]))<0.4
        elif MODE=='seg': keep=np.abs(S2(P2[:,0],P2[:,1],P2[:,2]))<0.4
        else: keep=np.zeros(len(P2),bool)
        pts=[p for p,k in zip(pts,keep) if k]; dirs=[d for d,k in zip(dirs,keep) if k]
    if pts and MODE!='none':
        vs=[];fs=[]
        for p,d in zip(pts,dirs):
            d=d/ (np.linalg.norm(d)+1e-9)
            a=d*0.14; up_=np.cross(d,[0.3,0.5,0.8]); up_/=np.linalg.norm(up_)+1e-9; b2=up_*0.035; c2=np.cross(d,up_)*0.035
            base=len(vs)
            for sx in(-1,1):
                for sy in(-1,1):
                    for sz in(-1,1): vs.append((p+sx*a+sy*b2+sz*c2).tolist())
            fs+= [[base+i for i in q] for q in [(0,1,3,2),(4,6,7,5),(0,4,5,1),(2,3,7,6),(0,2,6,4),(1,5,7,3)]]
        sm=bpy.data.meshes.new(name+'_st'); sm.from_pydata(vs,[],fs); sm.materials.append(STA)
        so=bpy.data.objects.new(name+'_st',sm); sc.collection.objects.link(so); so.location=offset
    return ob
for name,F,off,kind in parts:
    m=mesh_from(F,(xs,ys,zs),10)
    m=max(m.split(only_watertight=False),key=lambda q:len(q.faces))
    add_mesh(name,m,off,kind)
    print('part',name,len(m.faces),flush=True)
if MODE=='cuna':
    bpy.ops.mesh.primitive_uv_sphere_add(radius=NR,location=tuple(NOD+np.array([1.7,-1.5,0.3])),segments=48,ring_count=24)
    o=bpy.context.object; o.data.materials.append(NODM); bpy.ops.object.shade_smooth()
    # tilt surface bumps
    mod=o.modifiers.new('d','DISPLACE'); tex=bpy.data.textures.new('n','CLOUDS'); tex.noise_scale=0.25; mod.texture=tex; mod.strength=0.12
BRO=mat_simple('bronquio',(0.86,0.80,0.66,1),0.45); ART=mat_simple('arteria',(0.22,0.33,0.62,1),0.35); VEN=mat_simple('vena',(0.48,0.12,0.22,1),0.35)
def tube(pts,r,mat,off=(0,0,0),caps=True):
    cu=bpy.data.curves.new('t','CURVE'); cu.dimensions='3D'; cu.bevel_depth=r; cu.bevel_resolution=6; cu.use_fill_caps=caps
    sp=cu.splines.new('BEZIER'); sp.bezier_points.add(len(pts)-1)
    for bp,p in zip(sp.bezier_points,pts): bp.co=p; bp.handle_left_type=bp.handle_right_type='AUTO'
    o=bpy.data.objects.new('t',cu); o.data.materials.append(mat); sc.collection.objects.link(o); o.location=off; return o
def ring(p,d,r,off=(0,0,0)):
    tube([tuple(np.array(p)-0.06*np.array(d)),tuple(np.array(p)+0.06*np.array(d))],r*1.08,STA,off)
def stump(base,end,r,mat,off=(0,0,0)):
    tube([base,end],r,mat,off); d=np.array(end)-np.array(base); d=d/np.linalg.norm(d); ring(tuple(np.array(end)-0.1*d),d,r,off)
if MODE=='lob':
    # mediastinal trunks entering hilum (continue into lower lobe, hidden)
    tube([(-0.6,7.5,13.2),(-0.9,3.6,12.0),(-1.3,2.0,10.6),(-1.8,1.0,7.0)],0.62,BRO)
    tube([(1.0,7.5,12.6),(0.4,3.6,11.6),(-0.3,2.2,10.4),(-1.0,1.2,7.4)],0.55,ART)
    tube([(2.6,7.5,10.2),(2.3,3.6,10.4),(2.0,2.4,10.6)],0.45,VEN)
    S=[((-1.1,2.7,11.7),(-1.5,1.6,12.7),0.42,BRO),((0.3,3.0,11.6),(0.5,2.0,12.8),0.36,ART),((2.1,2.8,10.6),(2.5,1.8,11.6),0.34,VEN)]
    for b,e,r,m in S:
        stump(b,e,r,m)
        d=np.array(e)-np.array(b); d/=np.linalg.norm(d)
        stump(tuple(np.array(e)+1.5*d),tuple(np.array(e)-3.4*d-np.array([0,0,2.2])),r,m,LOBOFF)
if MODE=='seg':
    perp1=np.cross(AX,[0,0,1]); perp1/=np.linalg.norm(perp1); perp2=np.cross(AX,perp1)
    for k,(m,r,o) in enumerate([(BRO,0.34,perp1*0.0),(ART,0.29,perp1*0.75+perp2*0.25),(VEN,0.27,-perp1*0.75+perp2*0.3)]):
        b=HP-1.6*AX+o; e=HP+1.5*AX+o
        stump(tuple(b),tuple(e),r,m)
        stump(tuple(HP+3.6*AX+o),tuple(HP+1.85*AX+o),r,m,tuple(AX*4.6))
# world / lights / camera
sc.world=bpy.data.worlds.new('w'); sc.world.use_nodes=True
bg=sc.world.node_tree.nodes['Background']; bg.inputs[0].default_value=(1,1,1,1); bg.inputs[1].default_value=0.5
def light(loc,energy,size,col=(1,1,1)):
    l=bpy.data.lights.new('l','AREA'); l.energy=energy; l.size=size; l.color=col
    o=bpy.data.objects.new('l',l); sc.collection.objects.link(o); o.location=loc
    d=mathutils.Vector((0,0,11))-mathutils.Vector(loc); o.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
light((8,-30,30),5000,14); light((-25,-12,12),1600,10,(0.9,0.95,1)); light((10,20,25),2500,10)
cam=bpy.data.cameras.new('c'); cam.lens=52; co=bpy.data.objects.new('c',cam); sc.collection.objects.link(co)
LENS={'lob':44}
CP={'cuna':((34,-50,24),(2.5,-1,12)),'seg':((-24,-55,30),(-2,-1.5,13)),'lob':((10,-66,9),(0,-1.5,15.5)),'none':((6,-62,18),(0,0,11.5))}[MODE]
co.location=CP[0]; d=mathutils.Vector(CP[1])-mathutils.Vector(CP[0]); co.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
sc.camera=co; cam.lens=LENS.get(MODE,52)
sc.render.engine='CYCLES'; sc.cycles.samples=SAMPLES; sc.cycles.use_denoising=True
sc.render.resolution_x=1600; sc.render.resolution_y=1200; sc.render.film_transparent=True
sc.view_settings.view_transform='Standard'
sc.render.filepath=OUT; bpy.ops.render.render(write_still=True); print('done',OUT)
