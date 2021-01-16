from solid.utils import *
import solid
import os
from screw import MachineScrew,ScrewType
import utils
from const import *

ZERO_LENGTH=65
ZERO_WIDTH=30
ZERO_PLATE_HEIGHT=2.5
ZERO_SCREW_OFF = 3.5
ZERO_PLATE_TO_EDGE = (ZERO_LENGTH-ADAPTER_SIDE)/2
ZERO_SUPPORT_HEIGHT_TOP = 2.5
ZERO_SUPPORT_HEIGHT_BOTTOM = 2.5

def _zero_plate_base(support_height=0, screw_length=16, screw_offset=0, height=ZERO_PLATE_HEIGHT) -> solid.OpenSCADObject:
    support = solid.cylinder(d=6,h=support_height,center=False,segments=32)
    support_z = -support_height - height/2
    plate = utils.cube_chamfered([ZERO_LENGTH,ZERO_WIDTH,height],center=True,r=3),
    if support_height != 0:
        plate = solid.union()(
            plate,
            translate((ZERO_LENGTH/2-ZERO_SCREW_OFF,ZERO_WIDTH/2-ZERO_SCREW_OFF,support_z))(support),
            translate((ZERO_LENGTH/2-ZERO_SCREW_OFF,-ZERO_WIDTH/2+ZERO_SCREW_OFF,support_z))(support),
            translate((-ZERO_LENGTH/2+ZERO_SCREW_OFF,-ZERO_WIDTH/2+ZERO_SCREW_OFF,support_z))(support),
            translate((-ZERO_LENGTH/2+ZERO_SCREW_OFF,ZERO_WIDTH/2-ZERO_SCREW_OFF,support_z))(support),
        )
    return plate

def pi_zero_frontplate(gpio_opening=True,flex_cover=True, support_height=3.7):
    height = ZERO_PLATE_HEIGHT
    plate = _zero_plate_base(support_height=support_height, screw_offset=0, height=height)
    screw_obj = MachineScrew(type=ScrewType.M2_HEX,length=height+support_height-1,clearance=-0.2)
    screw = rotate([180,0,0])(screw_obj())
    plate = solid.difference()(
        plate,
        translate((ZERO_LENGTH/2-ZERO_SCREW_OFF,ZERO_WIDTH/2-ZERO_SCREW_OFF,-height/2-support_height))(screw),
        translate((ZERO_LENGTH/2-ZERO_SCREW_OFF,-ZERO_WIDTH/2+ZERO_SCREW_OFF,-height/2-support_height))(screw),
        translate((-ZERO_LENGTH/2+ZERO_SCREW_OFF,-ZERO_WIDTH/2+ZERO_SCREW_OFF,-height/2-support_height))(screw),
        translate((-ZERO_LENGTH/2+ZERO_SCREW_OFF,ZERO_WIDTH/2-ZERO_SCREW_OFF,-height/2-support_height))(screw),
    )
    if flex_cover:
        flex_cover = utils.cube_chamfered([ZERO_LENGTH,13,ZERO_PLATE_HEIGHT],center=True,r=3)
        plate += translate((10,0,0))(flex_cover)
    if gpio_opening:
        gpio_opening = translate((0,ZERO_WIDTH/2-GPIO_WIDTH/2-GPIO_OFFSET,0))(solid.cube([GPIO_LENGTH,GPIO_WIDTH,height],center=True))
        plate -= gpio_opening 
    return plate

def pi_zero_backplate():
    zero_plate = _zero_plate_base(support_height=ZERO_SUPPORT_HEIGHT_TOP, screw_offset=-.5)
    camera_plate = utils.cube_chamfered([ADAPTER_SIDE,ADAPTER_SIDE,ZERO_PLATE_HEIGHT],center=True,r=3)
    camera_plate = camera_plate + zero_plate
    screw_obj = MachineScrew(type=ScrewType.M2_HEX,length=ZERO_PLATE_HEIGHT*2,clearance=0)
    screw_bottom = rotate([180,0,0])(screw_obj())
    screw_top = MachineScrew(type=ScrewType.M2_HEX,length=ZERO_PLATE_HEIGHT*2,overhang=True)()
    camera_plate = solid.difference()(
        camera_plate,
        # Upper plate mount screws
        translate((ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-ZERO_PLATE_HEIGHT/2))(screw_bottom),
        translate((-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-ZERO_PLATE_HEIGHT/2))(screw_bottom),
        translate((ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-ZERO_PLATE_HEIGHT/2))(screw_bottom),
        translate((-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-ZERO_PLATE_HEIGHT/2))(screw_bottom),
        # Lens ring mount screws
        translate((0,CS_LENS_RING_NUT_OFFSET,-ZERO_PLATE_HEIGHT/2))(screw_bottom),
        translate((0,-CS_LENS_RING_NUT_OFFSET,-ZERO_PLATE_HEIGHT/2))(screw_bottom),
        # Pi mount screws
        translate((ZERO_LENGTH/2-ZERO_SCREW_OFF,ZERO_WIDTH/2-ZERO_SCREW_OFF,-.5))(screw_top),
        translate((ZERO_LENGTH/2-ZERO_SCREW_OFF,-ZERO_WIDTH/2+ZERO_SCREW_OFF,-.5))(screw_top),
        translate((-ZERO_LENGTH/2+ZERO_SCREW_OFF,-ZERO_WIDTH/2+ZERO_SCREW_OFF,-.5))(screw_top),
        translate((-ZERO_LENGTH/2+ZERO_SCREW_OFF,ZERO_WIDTH/2-ZERO_SCREW_OFF,-.5))(screw_top),
        # flex cable opening
        translate((ZERO_LENGTH/2-ZERO_PLATE_TO_EDGE/2,0,0))(cube([ZERO_PLATE_TO_EDGE,13,ZERO_PLATE_HEIGHT],center=True))
    )
    # flex cable cover
    flex_cover = utils.cube_chamfered([ZERO_LENGTH,13,ZERO_PLATE_HEIGHT-1.5],center=True,r=3)
    camera_plate += translate((10,0,0.75))(flex_cover)
    camera_plate -= translate((ADAPTER_SIDE/2-1.5,0,0))(cube([3,13,ZERO_PLATE_HEIGHT],center=True))
    camera_plate = rotate((180,0,0))(camera_plate)
    return camera_plate

if __name__ == "__main__":
    path = 'scad/board-plates'
    os.makedirs(path, exist_ok=True)
    plate = pi_zero_frontplate()
    plate = rotate((0,180,0))(plate)
    filename = 'pi_zero_frontplate.scad'
    solid.scad_render_to_file(plate, os.path.join(path,filename))
    plate = pi_zero_backplate()
    filename = 'pi_zero_backplate.scad'
    solid.scad_render_to_file(plate, os.path.join(path,filename))