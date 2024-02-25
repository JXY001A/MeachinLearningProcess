import numpy as np
import pygame, pygame.sndarray
from time import sleep

pygame.mixer.init(frequency=44100, size=-16, channels=1)

arr = np.random.randint(-32768,32767,size=44100) 
arr = arr.astype(np.int16)
sound = pygame.sndarray.make_sound(arr)
sound.play()
sleep(1)




