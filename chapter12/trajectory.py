from math import cos,sin,pi
def trajectory(theta,speed,height=0,dt=0.01,g=-9.81):
  vx = cos(theta * pi /180) * speed
  vz = sin(theta * pi /180) * speed
  
  t,x,z = 0,0,height
  
  ts,xs,zs = [t],[x],[z]
  
  while(z>0):
    t+=dt;
    vz += g * dt
    x += vx * dt
    z += vz * dt
    
    ts.append(t)
    xs.append(x)
    zs.append(z)
  return ts,xs,zs
    
  