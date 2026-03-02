import math

class Vector:
  def __init__(self,values):
    if not isinstance(values,list):
      raise TypeError("Values must be a list")
    if len(values)==0:
      raise TypeError("Vector can not be empty")
    self.values=values
  

  def __len__(self):
    return len(self.values)

  def __repr__(self):
    return f"Vector({self.values})"
  
  def dot(self,other):
    if len(self)!=len(other):
      raise TypeError("Vectors must be same length")
    res=0

    for i in range(len(self)):
      res+=self.values[i]*other.values[i]
    return res
  
  def magnitude(self):
    return math.sqrt(self.dot(self))
    
  def cosine_similarity(self,other):
    mag_s=self.magnitude()
    mag_o=self.magnitude()

    if mag_s==0 or mag_o==0:
      raise TypeError("Cosine similarity undefined for zero vectors")
    
    return self.dot(other)/(mag_s*mag_o)