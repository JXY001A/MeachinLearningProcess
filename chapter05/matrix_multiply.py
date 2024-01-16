
import sys
sys.path.append('/Users/jxy001a/Code/MeachinLearningProcess')

from chapter03.dot import dot

def matrix_multiply(a,b):
  return tuple(tuple(dot(row,col) for col in zip(*b)) for row in a)

# a= ((1,1,0),(1,0,1),(1,-1,-1))
# b= ((0,2,1),(0,1,0),(1,0,-1))

# print(matrix_multiply(a,b))
# print(list(zip(*b))) 


  