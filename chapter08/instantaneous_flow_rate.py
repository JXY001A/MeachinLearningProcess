from average_flow_rate import average_flow_rate;
from volume import volume,flow_rate;
from plot_function import plot_function

def instantaneous_flow_rate(v,t,digitals=6):
  tolerance = 10 ** (-digitals);
  h = 1;
  approx = average_flow_rate(v,t-h,t+h);
  
  for i in range(0,digitals*2):
    h = h/10;
    next_approx = average_flow_rate(v,t-h,t+h);
    if abs(next_approx - approx) < tolerance :
      return round(next_approx,digitals);
    else:
      approx = next_approx;
  raise Exception('Derivative did not converge');


def get_flow_rate_function(v):
  def flow_rate_function(t):
    return instantaneous_flow_rate(v,t);
  return flow_rate_function;



plot_function(flow_rate,0,10);
plot_function(get_flow_rate_function(volume),0,10);
