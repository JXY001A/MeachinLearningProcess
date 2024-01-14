from AppendixC import draw_teapot;
from math import pi;
import sys
sys.path.append('/Users/jxy001a/Code/MeachinLearningProcess')

from chapter02.rotate2D import rotate2d;

def rotate_z(angle,vector):
  x,y,z = vector;
  new_x,new_y = rotate2d(angle,(x,y));
  return (new_x,new_y,z);


scaled_triangles = [[rotate_z(pi/2,vertex) for vertex in triangles] for triangles in draw_teapot.original_triangles];
draw_teapot.draw_model(scaled_triangles);

