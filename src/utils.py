import solid
from solid.utils import *

def cube_chamfered(size: solid.ScadSize = None, center: bool = None, r: int = None) -> solid.OpenSCADObject:
    # segments = 64 - fillet
    # segments = 6 - chamfered

    segments = 32 
    if r == 0:
        return solid.cube(size, center)
    if len(size) > 2:
        h = size[2]
        l = size[0]
    else:
        h = size[0]
        l = size[0]
    w = size[1]
    c1 =  right(r)(forward(r)(solid.cylinder(center=center,r=r, h=h,segments=segments)))
    c2 =  right(l-r)(forward(r)(solid.cylinder(center=center,r=r, h=h, segments=segments)))
    c3 =  right(r)(forward(w-r)(solid.cylinder(center=center,r=r, h=h, segments=segments)))
    c4 =  right(l-r)(forward(w-r)(solid.cylinder(center=center,r=r, h=h, segments=segments)))
    cube = solid.hull().add([c1,c2,c3,c4])
    if center:
        cube = solid.translate((-size[0]/2,-size[1]/2,0))(cube)
    return cube