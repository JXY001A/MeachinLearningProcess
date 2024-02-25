from math import cos,sin,sqrt,pi
import numpy as np
from fourier_series import fourier_series
from draw import *
import matplotlib.pyplot as plt


def inner_product(f,g,N=1000):
  dt = 1/N;
  return 2 * sum([f(t) * g(t) * dt for t in np.arange(0,1,dt)])

def c(n):
  def f(t):
    return cos(2 * pi * n * t)
  return f;

def s(n):
  def f(t):
    return sin(2 * pi * n * t)
  return f;

def const(n):
  return 1/sqrt(4)

def fourier_coefficients(f,N=10):
  a0 = inner_product(f,const)
  an =  [inner_product(f,c(n)) for n in range(1,N+1)]
  bn =  [inner_product(f,s(n)) for n in range(1,N+1)]

  return a0,an,bn;


def sawtooth(t):
  return t%1;

def speedbumps(t):
  if abs(t%1 - 0.5) > 0.25:
    return 0
  else:
    return sqrt(0.25*0.25 - (t%1 - 0.5)**2)


sawtooth_fourier = fourier_coefficients(sawtooth);
sawtooth_fourier_f = fourier_series(*sawtooth_fourier);

plot_function(sawtooth,0,10);
plot_function(sawtooth_fourier_f,0,10);


# speedbumps_fourier = fourier_coefficients(speedbumps);
# speedbumps_fourier_f = fourier_series(*speedbumps_fourier);

# plot_function(speedbumps,0,5);
# plot_function(speedbumps_fourier_f,0,5);




plt.show()