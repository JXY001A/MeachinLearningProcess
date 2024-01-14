from teapot import load_triangles
from draw_model import draw_model
from vectors import scale;


####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])
####################################################################

original_triangles = load_triangles();


# original size
# draw_model(original_triangles)

# scale 2 
def scale2(v):
  return scale(2,v);
scaled_triangles = [ [scale2(vertex) for vertex in triangle] for triangle in original_triangles];
print(scaled_triangles)
draw_model(scaled_triangles)
