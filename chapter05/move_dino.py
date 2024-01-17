import sys;
sys.path.append('/Users/jxy001a/Code/MeachinLearningProcess')

from chapter03.draw3dUtils import *;
# from matrix_multiply import matrix_multiply ;
from chapter04.AppendixC.vectors import multiply_matrix_vector;



def dot(u,v):
  return sum(coord1* coord2 for coord1,coord2 in zip(u,v));

# def multiply_matrix_vector(a,b):
#   return tuple(dot(b,col) for col in zip(*a))

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

def polygon_segment_3d(points,color="blue"):
  count = len(points);
  return [Segment3D(points[i],points[(i+1) % count]) for i in range(0,count)];


dino_3d_vectors = [(x,y,1) for x,y in dino_vectors];

magic_matrix = ( 
  (1,0,3), 
  (0,1,1),
  (0,0,1));

def multiply_matrix_vector2(matrix,vector):
  middleVectors = tuple(tuple(vi * s for vi in v)  for s,v in zip(vector,zip(*matrix)))
  return  tuple(map(sum,zip(*middleVectors)))


translated_v = [multiply_matrix_vector2(magic_matrix,v) for v in dino_3d_vectors]

draw3d(
  Points3D(*translated_v,color="blue"),
  *polygon_segment_3d(translated_v,color="blue"),
  Points3D(*dino_3d_vectors,color="red"),
  *polygon_segment_3d(dino_3d_vectors,color="red")
);




# print(multiply_matrix_vector(magic_matrix,(0,-1,1)))
# print(multiply_matrix_vector2(magic_matrix,(0,-1,1)))



# print(sum(list((0,-1,1))))
# multiply_matrix_vector2(magic_matrix,(0,-1,1)); 
# print(list(zip(magic_matrix,(1,2,3))))
# draw3d(*polygon_segment_3d(dino_3d_vectors));

# print(zip(*(1,3,4)))


