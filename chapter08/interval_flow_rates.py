import numpy as np;
from average_flow_rate import average_flow_rate;
from volume import volume,plot_flow_rate;
import matplotlib.pyplot as plt


def interval_flow_rates(v,t1,t2,dt):
  return [(t,average_flow_rate(v,t,t+dt)) for t in np.arange(t1,t2,dt)];  

def plot_interval_flow_rates(v,t1,t2,dt):
  series = interval_flow_rates(v,t1,t2,dt);
  times = [t for (t,_) in series];
  rates = [r for (_,r) in series];
  
  plt.scatter(times,rates);
  plt.plot(times,rates)
  plt.show();
  

# plot_interval_flow_rates(volume,0,10,0.5);
# plot_flow_rate(volume,0,10,1);