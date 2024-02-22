from plot_function import plot_function
from math import *
from lading_position import lading_position

G = -9.81

def theta_to_deg(theta):
  return theta / 180 * pi;

def r(theta,v=20):
  return (-2 * (v ** 2) * sin(theta_to_deg(theta)) * cos(theta_to_deg(theta))) / G;


mock_lading_pos = lading_position();
# 绘制出落地位置与角度之间的变化
plot_function(r,0,90,mock_lading_pos);
  