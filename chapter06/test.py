from random import uniform;
from Vector2 import Vector2;
from math import isclose;

def random_scalar():
  return uniform(-10,10);

def random_vector2():
  return Vector2(random_scalar(),random_scalar())

def approx_equal_vector2(v,w):
  return  isclose(v.x,w.x) and isclose(v.y,w.y);


for _ in range(0,100):
  a = random_scalar();
  u,v = random_vector2(),random_vector2()
  assert approx_equal_vector2(a * (u+v) , a * v + a * u)