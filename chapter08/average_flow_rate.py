from volume import volume;
def average_flow_rate(v,t1,t2):
  return (v(t2)- v(t1)) / (t2-t1); 


# print(average_flow_rate(volume,4,9))