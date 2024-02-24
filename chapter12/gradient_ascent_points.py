from math import cos,sin,pi,sqrt
from vectors import to_polar, to_cartesian
from heat_map import scalar_field_heatmap
import matplotlib.pyplot as plt


B = 0.0004
C = 0.005
v = 20
g = -9.81

def length(v):
  return sqrt(sum([coord ** 2 for coord in v]))

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



def secant_slope(f,xmin,xmax):
  return (f(xmax) - f(xmin)) / (xmax-xmin)

def approx_derivative(f,x,dx=1e-6):
  return secant_slope(f,x-dx,x+dx)

def approx_gradient(f,x0,y0,dx=1e-6):
  partial_x = approx_derivative(lambda x: f(x,y0),x0,dx=dx)
  partial_y = approx_derivative(lambda y: f(x0,y),y0,dx=dx)
  
  return (partial_x,partial_y);



def gradient_ascent(f,x_start,y_start,tolerance=1e-6):
  x = x_start
  y = y_start
  
  grad = approx_gradient(f,x,y)
  
  while length(grad) > tolerance:
    x += grad[0]
    y += grad[1]
    grad = approx_gradient(f,x,y)
    
  return x,y


def gradient_ascent_points(f,xstart,ystart,tolerance=1e-6):
  x = xstart
  y = ystart
  xs, ys = [x], [y]
  grad = approx_gradient(f,x,y)
  while length(grad) > tolerance:
      x += grad[0]
      y += grad[1]
      grad = approx_gradient(f,x,y)
      xs.append(x)
      ys.append(y)
  return xs, ys


result = gradient_ascent(landing_distance,36,83);


scalar_field_heatmap(landing_distance,35,40,80,100)
plt.scatter([36,37.58114751557887],[83,89.99992616039857],c='k',s=75)
plt.plot(*gradient_ascent_points(landing_distance,36,83),c='k')
plt.xlabel('theta')
plt.ylabel('phi')
plt.gcf().set_size_inches(9,7)
plt.show()
    
  


