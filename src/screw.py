from enum import Enum
import solid
from solid.utils import *
import config

class ScrewType(Enum):
    M3_HEX = 1
    M2_5_HEX = 2
    M2_HEX = 3

screws = {
    ### Put actual dimensions
    ScrewType.M3_HEX : {'diameter': 3, 'head_diameter': 5.5, 'head_height': 4},
    ScrewType.M2_5_HEX : {'diameter': 2.5, 'head_diameter': 4.4, 'head_height': 2.5},
    ScrewType.M2_HEX : {'diameter': 2, 'head_diameter': 3.8, 'head_height': 2}
}

class Screw():
    def __init__(self, d: int, h_d: int, h_h:int):
        self.d = d
        self.head_d = h_d
        self.head_h = h_h

class MachineScrew(Screw):
    def __init__(self, 
    type: ScrewType = ScrewType.M3_HEX, 
    length=50,
    overhang=False,
    extend_head_height=0,
    clearance = 0.2,
    head_clearance = 0.3
    ):
       s = screws[type]
       self.d = s['diameter']
       self.head_d = s['head_diameter']
       if extend_head_height == 0:
            self.head_h = s['head_height']
       else:
            self.head_h = extend_head_height + s['head_height']
       self.clearance = clearance
       self.head_clearance = head_clearance
       self.length = length
       self.overhang = overhang

    def __call__(self) -> solid.OpenSCADObject:
        # Render screw head
        head = solid.cylinder(segments=config.segments, d=self.head_d+self.head_clearance,h=self.head_h) 
        shaft = solid.cylinder(segments=config.segments, d=self.d+self.clearance,h=self.length) 
        if self.overhang:
           layer_height = config.layer_height 
           cint = solid.cube([self.head_d*2,self.d,self.head_h],center=True)
           l1 = head*up(self.head_h/2)(cint)
           l2 = up(self.head_h/2)(solid.cube([self.d,self.d,self.head_h], center=True))
           head = head + down(layer_height)(l1)+down(layer_height*2)(l2)
        #    head = head + down(layer_height)(l1)
        # Put screw at zero z
        screw = head + down(self.length)(shaft)
        # return down(self.head_h)(screw)
        return screw 

if __name__ == "__main__":
    screw = MachineScrew(overhang=True, length=10)
    cube = down(5)(solid.cube(10, center=True))
    obj =  cube - down(3)(screw())

    solid.scad_render_to_file(obj, 'screw.scad')





