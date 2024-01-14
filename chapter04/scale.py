import sys;
from AppendixC import draw_teapot;
from AppendixC import vectors;


def scale2(v):
  return vectors.scale(2,v);


scaled_triangles = [[scale2(vertex) for vertex in triangles] for triangles in draw_teapot.original_triangles];
draw_teapot.draw_model(scaled_triangles);

