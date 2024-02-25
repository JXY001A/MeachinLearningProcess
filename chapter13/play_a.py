import numpy as np
import pygame, pygame.sndarray
from draw import *
from time import sleep

pygame.mixer.init(frequency=44100, size=-16, channels=1)


example = np.array([10000,-10000]).astype(np.int16)
form = np.repeat(example,50)
 
arr = np.tile(form,441)

sound = pygame.sndarray.make_sound(arr)
sound.play()
sleep(1)

# plot_sequence(form);







