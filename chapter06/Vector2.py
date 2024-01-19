from AbstractVector import AbstractVector;

class Vector2(AbstractVector):
  def __init__(self, x,y):
    self.x = x;
    self.y = y;
  
  def add(self,other):
    return Vector2(self.x+other.x,self.y + other.y)
  def scale(self, scalar):
    return Vector2(self.x * scalar , self.y * scalar)
  def __eq__(self,other):
    return self.x == other.x and self.y == other.y;
  def __repr__(self):
    return "Vector({},{})".format(self.x,self.y)
    

  
print(Vector2(1,3) - Vector2(5,1)) # (-4,2)


  