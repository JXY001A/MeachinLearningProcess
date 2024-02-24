from math import cos,sin,pi,sqrt

B = 0.0004
C = 0.005
v = 20
g = -9.81


def theta_to_deg(theta):
  return theta / 180 * pi;

def velocity_component(v,theta,phi):  
  vz = v * sin(theta_to_deg(theta))
  vxy = v * cos(theta_to_deg(theta)) 
  vy =  vxy * sin(theta_to_deg(phi))
  vx =  vxy * cos(theta_to_deg(phi))

  return vx,vy,vz,vxy


def landing_distance(theta,phi):
  vx,vy,vz,vxy = velocity_component(v,theta,phi)
  
  a = (g/2) - B*vx**2 + C*vy**2
  b = vz
  lading_time = -b/a;
  landing_distance_real = lading_time * vxy;
  
  return landing_distance_real




