class Matrix:
  def __init__(self,data):
    if not data or not isinstance(data,list):
      raise TypeError("Matrix must be an non-empty list")
    self.data=data
    self.rows=len(data)
    self.cols=len(data[0])

  def size(self):
    return (self.rows,self.cols)
  
  def transpose(self):
    res=[]
    for i in range(self.cols):
      k=[]
      for j in range(self.rows):
        k.append(self.data[j][i])
      res.append(k)
    return res

  def mul(self,other):
    if self.cols!=other.rows:
      raise TypeError("The matrix multiplication is not possible")
    res=[[0]*other.cols for _ in range(self.rows)]
    for i in range(self.rows):
      for j in range(other.cols):
        for k in range(self.cols):
          res[i][j]+=self.data[i][k]* other.data[k][j]
    return res
  
  def __repr__(self):
    return str(self.data)
