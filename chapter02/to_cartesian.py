# 极坐标 to 笛卡尔坐标
from math import sin,cos,pi

def to_cartesian(polar_vector):
    length,angle = polar_vector[0],polar_vector[1]
    return (length * cos(angle),length * sin(angle))

to_cartesian((5,37 * pi/180))