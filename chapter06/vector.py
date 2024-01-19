class Vector():
  def __init__(self,x,y):
    self.x = x;
    self.y = y;
  def add(self, v2):
    return Vector(self.x+v2.x,self.y+v2.y);
  def scale(self, scalar):
    return  Vector(self.x * scalar, self.y * scalar);
  def eq(self, other):
    return self.x == other.x and self.y == other.y;
  def __add__(self, v2):
    return self.add(v2);
  def __mul__(self, scalar):
    return self.scale(scalar);
  def __rmul__(self, scalar):
    return self.scale(scalar);
  def __repr__(self):
    return "Vector({},{})".format(self.x,self.y)


print(3.0 * Vector(1,0) + 4 * Vector(0,1) ) # Vector(3.0,4.0)


  
  