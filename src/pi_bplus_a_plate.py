from solid.utils import *
import solid
import os
from screw import MachineScrew,ScrewType
import utils
from const import *

B_LENGTH = 85
B_WIDTH = 56
B_SCREW_OFF = 3.5
B_SCREW_DISTANCE_X = 58
B_SCREW_DISTANCE_Y = 49
B_PLATE_HEIGHT = 2.5

def pi_bplus_a_frontplate(height=2.5, gpio_opening=True):
    support_height = 12
    # This is basically only the aray from screw to screw, we only care about that area
    length = B_SCREW_DISTANCE_X + 2*B_SCREW_OFF
    width = B_WIDTH
    support_z = -support_height - height/2
    plate = utils.cube_chamfered([length,width,height],center=True,r=3)
    screw_obj = MachineScrew(type=ScrewType.M2_HEX,length=support_height,clearance=-0.2)
    screw_bottom = rotate([180,0,0])(screw_obj())
    support = solid.cylinder(d=6,h=support_height,center=False,segments=32)
    plate = solid.union()(
        plate,
        translate((length/2-B_SCREW_OFF,width/2-B_SCREW_OFF,support_z))(support),
        translate((length/2-B_SCREW_OFF,-width/2+B_SCREW_OFF,support_z))(support),
        translate((-length/2+B_SCREW_OFF,-width/2+B_SCREW_OFF,support_z))(support),
        translate((-length/2+B_SCREW_OFF,width/2-B_SCREW_OFF,support_z))(support),
    )
    plate = solid.difference()(
        plate,
        # Upper plate mount screws
        translate((ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-height/2))(screw_bottom),
        translate((-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-height/2))(screw_bottom),
        translate((ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-height/2))(screw_bottom),
        translate((-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-height/2))(screw_bottom),
        # Lens ring mount screws
        translate((CS_LENS_RING_NUT_OFFSET,0,-height/2))(screw_bottom),
        translate((-CS_LENS_RING_NUT_OFFSET,0,-height/2))(screw_bottom),
        # Pi mount screws
        translate((length/2-B_SCREW_OFF,width/2-B_SCREW_OFF,-support_height-screw_obj.head_h))(screw_bottom),
        translate((length/2-B_SCREW_OFF,-width/2+B_SCREW_OFF,-support_height-screw_obj.head_h))(screw_bottom),
        translate((-length/2+B_SCREW_OFF,-width/2+B_SCREW_OFF,-support_height-screw_obj.head_h))(screw_bottom),
        translate((-length/2+B_SCREW_OFF,width/2-B_SCREW_OFF,-support_height-screw_obj.head_h))(screw_bottom),
        # flex cable opening
        translate((0,ADAPTER_SIDE/2-2.5,0))(cube([16.5,2,height],center=True))
    )
    if gpio_opening:
        gpio_opening = translate((0.3,-(width/2 - GPIO_WIDTH/2 - 0.8),0))(solid.cube([GPIO_LENGTH,GPIO_WIDTH,height],center=True))
        plate -= gpio_opening 
    return plate


def pi_bplus_a_backplate(height=2.5):
    support_height = 3
    full_length = B_LENGTH
    width = B_WIDTH
    support_z = -support_height - height/2
    plate = utils.cube_chamfered([full_length,width,height],center=True,r=3)
    screw_top = MachineScrew(type=ScrewType.M2_HEX,length=support_height*2,overhang=True)()
    support = solid.cylinder(d=6,h=support_height,center=False,segments=32)
    screw_x = full_length/2-B_SCREW_OFF
    plate = solid.union()(
        plate,
        translate((screw_x,width/2-B_SCREW_OFF,support_z))(support),
        translate((screw_x,-width/2+B_SCREW_OFF,support_z))(support),
        translate((screw_x-B_SCREW_DISTANCE_X,width/2-B_SCREW_OFF,support_z))(support),
        translate((screw_x-B_SCREW_DISTANCE_X,-width/2+B_SCREW_OFF,support_z))(support),
    )
    plate = solid.difference()(
        plate,
        translate((screw_x,width/2-B_SCREW_OFF,0))(screw_top),
        translate((screw_x,-width/2+B_SCREW_OFF,0))(screw_top),
        translate((screw_x-B_SCREW_DISTANCE_X,-width/2+B_SCREW_OFF,0))(screw_top),
        translate((screw_x-B_SCREW_DISTANCE_X,width/2-B_SCREW_OFF,0))(screw_top),
    )
    return plate

if __name__ == "__main__":
    path = 'scad/board-plates'
    os.makedirs(path, exist_ok=True)
    plate = pi_bplus_a_backplate()
    plate = rotate((0,180,0))(plate)
    filename = 'pi_bplus_backplate.scad'
    solid.scad_render_to_file(plate, os.path.join(path,filename))
    plate = pi_bplus_a_frontplate()
    plate = rotate((0,180,0))(plate)
    filename = 'pi_bplus_a_frontplate.scad'
    solid.scad_render_to_file(plate, os.path.join(path,filename))