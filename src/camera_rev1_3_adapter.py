from solid.utils import *
import solid
import os
from screw import MachineScrew,ScrewType
import utils
from const import *

def camera_rev_1_3_adapter():
    height = 7.5 
    sensor_h = 3
    sensor_w = 8.75 + 0.35
    sensor_l = 8.65 + 0.35
    module_w = 24 
    module_l = 25
    sensor_y_off_top = 6.1
    sensor_y_center_offset = (24 - 8.75)/2 - sensor_y_off_top
    screw_top_y_offset = 9.4
    screw_top_x_offset = 2.2
    screw_bottom_y_offset = 1.8
    screw_bottom_x_offset = 2
    # led_bottom_offset_x = 4.4
    # led_bottom_offset_y = 4.2
    # sensor_y =  PLATE_SIDE/2-sensor_w/2 - (PLATE_SIDE-module_l)/2-sensor_y_off
    # sensor_y = PLATE_SIDE/2-sensor_w/2 - (PLATE_SIDE-module_l)/2 -sensor_y_off_top
    plate = utils.cube_chamfered([ADAPTER_SIDE,ADAPTER_SIDE,height],center=True,r=3)
    plate = translate((0,0,height/2))(plate)
    sensor = cube([sensor_l,sensor_w,height+0.1],center=True)
    conn_cutout = cube([sensor_l,module_w/2+0.5,height],center=True)
    led_pocket = cylinder(segments=32,d=5,h=height,center=True)
    board = union()(
        translate((0,0,height/2+sensor_h))(cube([module_l+0.5,module_w+0.5,height],center=True)),
        # connector cutout
        translate((0,-module_w/4,height/2+sensor_h-2))(conn_cutout),
        # mounting screws
        translate((module_l/2-screw_top_x_offset,module_w/2-screw_top_y_offset,height/2+0.4))(cylinder(segments=32,d=2,h=height,center=True)),
        translate((-module_l/2+screw_top_x_offset,module_w/2-screw_top_y_offset,height/2+0.4))(cylinder(segments=32,d=2,h=height,center=True)),
        translate((-module_l/2+screw_bottom_x_offset,-module_w/2+screw_bottom_y_offset,height/2+0.4))(cylinder(segments=32,d=2,h=height,center=True)),
        translate((module_l/2-screw_bottom_x_offset,-module_w/2+screw_bottom_y_offset,height/2+0.4))(cylinder(segments=32,d=2,h=height,center=True)),
        # smd led and resistor pocket
        translate((module_l/2-5,-module_w/2+3.75,sensor_h*2-1))(led_pocket),
        # led opening
        # translate((module_l/2-led_bottom_offset_x,-module_w/2+led_bottom_offset_y,0))(cylinder(segments=32,d=2,h=height,center=True))
    )
    screw_hole = MachineScrew(type=ScrewType.M2_HEX,length=height*2,overhang=True,extend_head_height=height)()
    screw_hole = rotate([180,0,0])(screw_hole)
    plate = difference()(
        plate,
        translate((0,-sensor_y_center_offset))(board),
        # make space for flex cable
        translate((0,ADAPTER_SIDE/4-1,height/2+sensor_h))(cube([module_l+0.5,ADAPTER_SIDE/2,height],center=True)),
        sensor,
        # mounting screws
        translate((ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,4))(screw_hole),
        translate((-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,4))(screw_hole),
        translate((ADAPTER_SIDE/2-ADAPTER_HOLE_TO_SIDE,-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,4))(screw_hole),
        translate((-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,-ADAPTER_SIDE/2+ADAPTER_HOLE_TO_SIDE,4))(screw_hole),
        # Lens ring mount screws
        translate((CS_LENS_RING_NUT_OFFSET,0,-.4))(screw_hole),
        translate((-CS_LENS_RING_NUT_OFFSET,0,-.4))(screw_hole),
    )
    return plate

if __name__ == "__main__":
    adapter = camera_rev_1_3_adapter()
    filename = 'camera_rev_1_3_adapter.scad'
    path = 'scad/adapters'
    os.makedirs(path, exist_ok=True)
    solid.scad_render_to_file(adapter, os.path.join(path,filename))