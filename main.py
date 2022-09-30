import numpy
print("2x+3y=5")
print("5x-6y=9")
A = numpy.array([[2, 3], [5, -6]])
B = numpy.array([5, 9])
print(numpy.linalg.solve(A,B))
