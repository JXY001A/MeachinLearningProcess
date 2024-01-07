# 提供 atan2 方法直接转换极坐标为笛卡尔坐标系 
from math import atan2,sqrt

def length(vector):
    return sqrt(vector[0]**2 + vector[1]**2);

def to_polar(vector):
    x,y = vector[0],vector[1]
    angle =  atan2(y,x);
    return (length(vector),angle);

to_polar((1,0)) == (1,0)
