from math import sin,pi
from draw import *
import pygame, pygame.sndarray
from time import sleep



pygame.mixer.init(frequency=44100, size=-16, channels=1)

def make_sinusoid(frequency,amplitude):
  def f(t):
    return amplitude * sin(2 * pi *  frequency * t)
  return f

# plot_function(make_sinusoid(5,4),0,1)

def simple(f,start,end,count):
  mapf = np.vectorize(f)
  
  ts = np.arange(start,end,(end-start)/count)
  
  values = mapf(ts)
  
  return values.astype(np.int16)




sinusoid = make_sinusoid(441,10000)
arr = simple(sinusoid,0,1,44100)
# print(arr)

sound = pygame.sndarray.make_sound(arr)
sound.play()
sleep(1)