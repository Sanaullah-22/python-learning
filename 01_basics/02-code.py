# Radius to Area
from math import pi    # import pi
#sqr function
def square(x):
    return x * x
#area function
def area(r):
    return pi*square(r)
result=area(22)
print("Area is",result)
