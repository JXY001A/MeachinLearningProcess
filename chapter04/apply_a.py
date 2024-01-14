from AppendixC import vectors;

from AppendixC import draw_teapot;
from math import pi;
# import sys
# sys.path.append('/Users/jxy001a/Code/MeachinLearningProcess')


Ae1 = (1,1,1);
Ae2 = (1,0,-1);
Ae3 = (0,1,1);

def apply_a(v):
  return vectors.add(
    vectors.scale(v[0],Ae1),
    vectors.scale(v[1],Ae2),
    vectors.scale(v[2],Ae3),
  );

scaled_triangles = [[apply_a(vertex) for vertex in triangles] for triangles in draw_teapot.original_triangles];
draw_teapot.draw_model(scaled_triangles);

