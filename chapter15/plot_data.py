import matplotlib.pyplot as plt
def plot_data(ds):
  plt.scatter([d[0] for d in ds if d[2]==0],[d[1] for d in ds if d[2]==0],c='C1')
  plt.scatter([d[0] for d in ds if d[2]==1],[d[1] for d in ds if d[2]==1],c='C0',marker='x')
  plt.ylabel("Price ($)",fontsize=16)
  plt.xlabel("Odometer (mi)",fontsize=16)