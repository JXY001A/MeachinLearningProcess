from plot_function import plot_flow_rate,plot_volume,plot_function;


def volume(t):
    return (t-4)**3 / 64 + 3.3

def flow_rate(t):
    return 3*(t-4)**2 / 64
  
# plot_volume(volume,0,10);
# plot_flow_rate(flow_rate,0,10);