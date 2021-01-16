from solid.utils import *
import solid
import os
from screw import MachineScrew,ScrewType
import utils
from const import *

CAMERA_SIDE = 8.6+0.15
ADAPTER_HEIGHT = 3.1

def camera_flex_adapter():
    plate = utils.cube_chamfered([ADAPTER_SIDE,ADAPTER_SIDE,ADAPTER_HEIGHT],center=False,r=3)
    screw_hole = MachineScrew(type=ScrewType.M2_HEX,length=ADAPTER_HEIGHT*2,overhang=True)()
    screw_hole = rotate([180,0,0])(screw_hole)
    plate -= translate((ADAPTER_HOLE_TO_SIDE,ADAPTER_HOLE_TO_SIDE,1))(screw_hole())
    plate -= translate((ADAPTER_SIDE-ADAPTER_HOLE_TO_SIDE,4,1))(screw_hole())
    plate -= translate((4,ADAPTER_SIDE-ADAPTER_HOLE_TO_SIDE,1))(screw_hole())
    plate -= translate((ADAPTER_SIDE-ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE-ADAPTER_HOLE_TO_SIDE,1))(screw_hole())
    camera_body = solid.cube([CAMERA_SIDE,CAMERA_SIDE,ADAPTER_HEIGHT+0.1],center=False)()
    camera_body += translate((0,CAMERA_SIDE,ADAPTER_HEIGHT-2))(cube([CAMERA_SIDE,3.5,2]))
    camera_body += translate(((CAMERA_SIDE-6)/2,CAMERA_SIDE+2,ADAPTER_HEIGHT-0.4))(cube([6,16,0.5]))
    camera_body = translate((ADAPTER_SIDE/2-CAMERA_SIDE/2,ADAPTER_SIDE/2-CAMERA_SIDE/2,0))(camera_body)
    plate -= camera_body
    plate -= translate((ADAPTER_SIDE/2-CS_LENS_RING_NUT_OFFSET,ADAPTER_SIDE/2,-ADAPTER_HEIGHT/2))(screw_hole)
    plate -= translate((ADAPTER_SIDE/2+CS_LENS_RING_NUT_OFFSET,ADAPTER_SIDE/2,-ADAPTER_HEIGHT/2))(screw_hole)
    return plate

if __name__ == "__main__":
    adapter = camera_flex_adapter()
    filename = 'camera_flex_adapter.scad'
    path = 'scad/adapters'
    os.makedirs(path, exist_ok=True)
    solid.scad_render_to_file(adapter, os.path.join(path,filename))