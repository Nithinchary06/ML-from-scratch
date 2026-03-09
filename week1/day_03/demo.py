from mat import Matrix

A = Matrix([
    [2,3],
    [1,4]
])

B = Matrix([
    [5,6],
    [7,8]
])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Multiplication:")
print(A.multiply(B))

print("Transpose:")
print(A.transpose())

print("Determinant:")
print(A.det2x2())

print("Inverse:")
print(A.inverse2x2())

print("Is Singular:")
print(A.is_singular())