# MODULES IN PYTHON
# A module is a python containing python statements , variale, functions , classes
# Ready made modules
# User - Defined Modules
# import statements are used to call modules


import math
help(math)
from math import pow, sqrt, sin


# import os
# help(os)


# power = pow(8,  2)
# print(power)
#
# print(sqrt(400))
# print(sin(90))

# volumes of figures

def cuboid(l, w, h):
    return l*w*h

def sphere(r):
    PI = 3.142
    answer = 4/3 * PI * r**3
    return answer

def cylinder(r,h):
    PI = 3.142
    results = PI *(r**2) * h
    return results
