
from numpy import arange;
from plot_function import plot_flow_rate,plot_volume,plot_function;
from volume import flow_rate,volume;


def small_volume_change(q,t,dt):
  return q(t) * dt;

def volume_change(q,t1,t2,dt):
  return sum(small_volume_change(q,t,dt) for t in  arange(t1,t2,dt));

def approximate_volume(q,v0,dt,T): 
  return v0 + volume_change(q,0,T,dt)


def approximate_volume_function(q,v0,dt):
  def volume_function(T):
    return approximate_volume(q,v0,dt,T);
  return volume_function;
  
plot_function(approximate_volume_function(flow_rate,2.3,0.5),0,10);
plot_function(volume,0,10);
