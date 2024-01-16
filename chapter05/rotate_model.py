
from math import cos,sin;
import sys
sys.path.append('/Users/jxy001a/Code/MeachinLearningProcess')
from chapter04.AppendixC import draw_teapot;


def get_rotation_matrix(t):
  # TODO: 毫秒转秒
  seconds = t/1000;
  return (
    (cos(seconds),0,-sin(seconds)),
    ((0,1,0)),
    (sin(seconds),0,cos(seconds))
  );


draw_teapot.draw_model(draw_teapot.original_triangles,get_matrix=get_rotation_matrix);

