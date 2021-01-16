import sys

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

this.layer_height = 0.2
this.segments = 32