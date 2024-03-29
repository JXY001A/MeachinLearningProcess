import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from math import sin, cos, pi

def plot_function(f,xmin,xmax,mock_lading_pos,**kwargs):
  ts = np.linspace(xmin,xmax,1000)
  plt.plot(ts,[f(t) for t in ts],**kwargs)
  if mock_lading_pos :
    plt.scatter(mock_lading_pos[0],mock_lading_pos[1]);
  plt.show()