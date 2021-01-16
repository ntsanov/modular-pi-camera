from solid.utils import *
import solid
import os
from screw import MachineScrew,ScrewType
import utils
from const import *

ADAPTER_TO_SENSOR = 3.1
CS_LENS_RING_H= CS_MOUNT_FOCAL_DISTANCE - ADAPTER_TO_SENSOR + SENSOR_BASE_HEIGHT

def cs_mount_ring(height=CS_LENS_RING_H):
    outside = solid.cylinder(segments=128,d=CS_LENS_RING_OD,h=height,center=True)
    inside = solid.cylinder(segments=128,d=CS_LENS_RING_ID,h=height+0.1,center=True)
    ring = outside-inside
    split_block = cube((10,10,height),center=True)
    ring = ring + translate((0,CS_LENS_RING_OD/2,0))(split_block)
    # split = forward(LENS_RING_OD/2)(cube([1,LENS_RING_OD/2,height+0.1], center=True))
    # ring = ring - split
    screw = MachineScrew(type=ScrewType.M2_HEX,length=10,extend_head_height=10)()
    screw_rotated = rotate((0,90,0))(MachineScrew(type=ScrewType.M2_5_HEX,length=10,extend_head_height=10,head_clearance=0.3)())
    # ring -= translate((2.7,LENS_RING_OD/2+2,0))(screw_rotated)
    nut = rotate((0,90,0))(solid.cylinder(d=M2_5_NUT_D,h=M2_5_NUT_H,segments=6,center=True))
    screw_parallel = rotate((90,0,0))(screw)
    nut_parallel = rotate((0,90,90))(solid.cylinder(d=M2_NUT_D,h=M2_NUT_H+2,segments=6,center=True))
    ring = solid.difference()(
        ring,
        # Split
        forward(CS_LENS_RING_OD/2)(cube([1,CS_LENS_RING_OD/2,height+0.1], center=True)),
        # Tightening screw
        translate((2.7,CS_LENS_RING_OD/2+2,0))(screw_rotated),
        # Tightening nut
        translate((-5+M2_5_NUT_H/2,CS_LENS_RING_OD/2+2,0))(nut),
        # Mounting screws
        translate((CS_LENS_RING_NUT_OFFSET,0,height/2-4))(screw),
        translate((-CS_LENS_RING_NUT_OFFSET,0,height/2-4))(screw),
        # side mount
        rotate((0,0,35))(back(CS_LENS_RING_OD/2)(screw_parallel)),
        rotate((0,0,35))(back(CS_LENS_RING_ID/2+1.2)(nut_parallel)),
        rotate((0,0,-35))(back(CS_LENS_RING_OD/2)(screw_parallel)),
        rotate((0,0,-35))(back(CS_LENS_RING_ID/2+1.2)(nut_parallel)),
    )
    return ring


if __name__ == "__main__":
    adapter = cs_mount_ring()
    filename = 'cs-lens-mount.scad'
    path = 'scad/lens-mounts'
    os.makedirs(path, exist_ok=True)
    solid.scad_render_to_file(adapter, os.path.join(path,filename))
