from plot_function import *
from math import *

G = -9.81
def theta_to_deg(theta):
  return theta / 180 * pi;

def z(t,v=20,theta=45):
  return v * sin(theta_to_deg(theta)) * t + (G* t**2)/2

plot_function(z,0,2.9) 
  