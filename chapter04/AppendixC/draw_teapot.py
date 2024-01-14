from .teapot import load_triangles
from .draw_model import draw_model


####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
from . import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])
####################################################################

original_triangles = load_triangles();



