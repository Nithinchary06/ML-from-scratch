from vectors import Vector

v1=Vector([1,2,3])
v2=Vector([4,5,6])

print("Vector v1:",v1)
print("Vector v2:",v2)

print("Dot Product:",v1.dot(v2))
print("Magnitude of v1",v1.magnitude())
print("Cosine similarity:",v1.cosine_similarity(v2))