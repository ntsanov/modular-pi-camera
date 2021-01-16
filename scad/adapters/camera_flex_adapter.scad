// Generated by SolidPython 1.0.4 on 2021-01-16 14:00:08


difference() {
	hull() {
		translate(v = [3, 0, 0]) {
			translate(v = [0, 3, 0]) {
				cylinder($fn = 32, center = false, h = 3.1000000000, r = 3);
			}
		}
		translate(v = [35, 0, 0]) {
			translate(v = [0, 3, 0]) {
				cylinder($fn = 32, center = false, h = 3.1000000000, r = 3);
			}
		}
		translate(v = [3, 0, 0]) {
			translate(v = [0, 35, 0]) {
				cylinder($fn = 32, center = false, h = 3.1000000000, r = 3);
			}
		}
		translate(v = [35, 0, 0]) {
			translate(v = [0, 35, 0]) {
				cylinder($fn = 32, center = false, h = 3.1000000000, r = 3);
			}
		}
	}
	translate(v = [4.0000000000, 4.0000000000, 1]) {
		rotate(a = [180, 0, 0]) {
			union() {
				cylinder($fn = 32, d = 4.1000000000, h = 2);
				translate(v = [0, 0, -0.2000000000]) {
					intersection() {
						cylinder($fn = 32, d = 4.1000000000, h = 2);
						translate(v = [0, 0, 1.0000000000]) {
							cube(center = true, size = [7.6000000000, 2, 2]);
						}
					}
				}
				translate(v = [0, 0, -0.4000000000]) {
					translate(v = [0, 0, 1.0000000000]) {
						cube(center = true, size = [2, 2, 2]);
					}
				}
				translate(v = [0, 0, -6.2000000000]) {
					cylinder($fn = 32, d = 2.2000000000, h = 6.2000000000);
				}
			}
		}
	}
	translate(v = [34.0000000000, 4, 1]) {
		rotate(a = [180, 0, 0]) {
			union() {
				cylinder($fn = 32, d = 4.1000000000, h = 2);
				translate(v = [0, 0, -0.2000000000]) {
					intersection() {
						cylinder($fn = 32, d = 4.1000000000, h = 2);
						translate(v = [0, 0, 1.0000000000]) {
							cube(center = true, size = [7.6000000000, 2, 2]);
						}
					}
				}
				translate(v = [0, 0, -0.4000000000]) {
					translate(v = [0, 0, 1.0000000000]) {
						cube(center = true, size = [2, 2, 2]);
					}
				}
				translate(v = [0, 0, -6.2000000000]) {
					cylinder($fn = 32, d = 2.2000000000, h = 6.2000000000);
				}
			}
		}
	}
	translate(v = [4, 34.0000000000, 1]) {
		rotate(a = [180, 0, 0]) {
			union() {
				cylinder($fn = 32, d = 4.1000000000, h = 2);
				translate(v = [0, 0, -0.2000000000]) {
					intersection() {
						cylinder($fn = 32, d = 4.1000000000, h = 2);
						translate(v = [0, 0, 1.0000000000]) {
							cube(center = true, size = [7.6000000000, 2, 2]);
						}
					}
				}
				translate(v = [0, 0, -0.4000000000]) {
					translate(v = [0, 0, 1.0000000000]) {
						cube(center = true, size = [2, 2, 2]);
					}
				}
				translate(v = [0, 0, -6.2000000000]) {
					cylinder($fn = 32, d = 2.2000000000, h = 6.2000000000);
				}
			}
		}
	}
	translate(v = [34.0000000000, 34.0000000000, 1]) {
		rotate(a = [180, 0, 0]) {
			union() {
				cylinder($fn = 32, d = 4.1000000000, h = 2);
				translate(v = [0, 0, -0.2000000000]) {
					intersection() {
						cylinder($fn = 32, d = 4.1000000000, h = 2);
						translate(v = [0, 0, 1.0000000000]) {
							cube(center = true, size = [7.6000000000, 2, 2]);
						}
					}
				}
				translate(v = [0, 0, -0.4000000000]) {
					translate(v = [0, 0, 1.0000000000]) {
						cube(center = true, size = [2, 2, 2]);
					}
				}
				translate(v = [0, 0, -6.2000000000]) {
					cylinder($fn = 32, d = 2.2000000000, h = 6.2000000000);
				}
			}
		}
	}
	translate(v = [14.6250000000, 14.6250000000, 0]) {
		union() {
			cube(center = false, size = [8.7500000000, 8.7500000000, 3.2000000000]);
			translate(v = [0, 8.7500000000, 1.1000000000]) {
				cube(size = [8.7500000000, 3.5000000000, 2]);
			}
			translate(v = [1.3750000000, 10.7500000000, 2.7000000000]) {
				cube(size = [6, 16, 0.5000000000]);
			}
		}
	}
	translate(v = [3.7250000000, 19.0000000000, -1.5500000000]) {
		rotate(a = [180, 0, 0]) {
			union() {
				cylinder($fn = 32, d = 4.1000000000, h = 2);
				translate(v = [0, 0, -0.2000000000]) {
					intersection() {
						cylinder($fn = 32, d = 4.1000000000, h = 2);
						translate(v = [0, 0, 1.0000000000]) {
							cube(center = true, size = [7.6000000000, 2, 2]);
						}
					}
				}
				translate(v = [0, 0, -0.4000000000]) {
					translate(v = [0, 0, 1.0000000000]) {
						cube(center = true, size = [2, 2, 2]);
					}
				}
				translate(v = [0, 0, -6.2000000000]) {
					cylinder($fn = 32, d = 2.2000000000, h = 6.2000000000);
				}
			}
		}
	}
	translate(v = [34.2750000000, 19.0000000000, -1.5500000000]) {
		rotate(a = [180, 0, 0]) {
			union() {
				cylinder($fn = 32, d = 4.1000000000, h = 2);
				translate(v = [0, 0, -0.2000000000]) {
					intersection() {
						cylinder($fn = 32, d = 4.1000000000, h = 2);
						translate(v = [0, 0, 1.0000000000]) {
							cube(center = true, size = [7.6000000000, 2, 2]);
						}
					}
				}
				translate(v = [0, 0, -0.4000000000]) {
					translate(v = [0, 0, 1.0000000000]) {
						cube(center = true, size = [2, 2, 2]);
					}
				}
				translate(v = [0, 0, -6.2000000000]) {
					cylinder($fn = 32, d = 2.2000000000, h = 6.2000000000);
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
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
    path = 'stl/adapters'
    os.makedirs(path, exist_ok=True)
    solid.scad_render_to_file(adapter, os.path.join(path,filename)) 
 
************************************************/
