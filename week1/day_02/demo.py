from mat import Matrix

n,m=map(int,input().split())
a=[]
for _ in range(n):
  a.append(list(map(int,input().split())))

A=Matrix(a)
n,m=map(int,input().split())
b=[]
for _ in range(n):
  b.append(list(map(int,input().split())))

B=Matrix(b)

mul=A.mul(B)

print(mul)

print(A.transpose())