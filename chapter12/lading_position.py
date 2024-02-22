import matplotlib.pyplot as plt
from trajectory  import trajectory,lading_pos
def lading_position(): 
  angles = range(0,90,5)
  positions = [lading_pos(trajectory(angle)) for angle in angles]
  return [angles,positions]