from math import cos,sin,pi
from plot_trajectories import *
def trajectory(theta,speed=20,height=0,dt=0.01,g=-9.81):
  vx = cos(theta * pi /180) * speed
  vz = sin(theta * pi /180) * speed
  
  t,x,z = 0,0,height
  
  ts,xs,zs = [t],[x],[z]
  
  while(z>=0):
    t+=dt;
    vz += g * dt
    x += vx * dt
    z += vz * dt
    
    ts.append(t)
    xs.append(x)
    zs.append(z)
  
  return ts,xs,zs
    
  
# trajectory(45)
# plot_trajectories(trajectory(45),trajectory(60))
def lading_pos(traj):
  return traj[1][-1]  

def hang_time(traj):
  return traj[0][-1] 


def max_height(traj):
  return traj[2][-1]  