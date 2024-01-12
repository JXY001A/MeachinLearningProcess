from length import length;
from math import acos,pi;
from dot import dot;

def cos_deg(v1,v2):
  return dot(v1,v2)/length(v1)*length(v2);

def angle_between(v1,v2):
  return acos(cos_deg(v1,v2));

print(cos_deg((1,0),(0,2)))
print(cos_deg((1,0),(2,0)))
# print()
# angle_between((1,0),(0,1))