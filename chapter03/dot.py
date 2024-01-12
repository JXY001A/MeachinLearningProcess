# 求点积
def dot(u,v):
  return sum(coord1* coord2 for coord1,coord2 in zip(u,v));

# print(
#   dot((1,0),(0,2)) == 0
# )

# print(
#   dot((0,3,0),(0,0,2)) == 0
# )
