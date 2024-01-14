from AppendixC import draw_teapot;
from math import pi;
import sys
sys.path.append('/Users/jxy001a/Code/MeachinLearningProcess')

from chapter02.rotate2D import rotate2d;

def rotate_x(angle,vector):
  x,y,z = vector;
  new_y,new_z = rotate2d(angle,(y,z));
  return (x,new_y,new_z);


scaled_triangles = [[rotate_x(pi/4,vertex) for vertex in triangles] for triangles in draw_teapot.original_triangles];
draw_teapot.draw_model(scaled_triangles);

