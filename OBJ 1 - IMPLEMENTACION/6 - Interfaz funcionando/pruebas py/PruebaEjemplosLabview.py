import math
from collections import namedtuple

def Add(a, b):
	return a + b

def ConcatenateStrings(str1, str2):
	return str1 + str2

def EuclideanDistance(point1, point2):
	xDiff = point1[0] - point2[0]
	yDiff = point1[1] - point2[1]
	return math.sqrt(xDiff * xDiff + yDiff * yDiff)

def AppendToList(array, newElement):
	array.append(newElement)

def CrossProduct(vector1, vector2):
	i = vector1.j * vector2.k - vector1.k * vector2.j
	j = vector1.k * vector2.i - vector1.i * vector2.k
	k = vector1.i * vector2.j - vector1.j * vector2.i
	return namedtuple('Vector', ['i', 'j', 'k'])(i, j, k)

# Testing the functions

# Test Add function
print("Add(5, 3):", Add(5, 3))  # Expected output: 8
print("Add(2.5, 4.5):", Add(2.5, 4.5))  # Expected output: 7.0

# Test ConcatenateStrings function
print("ConcatenateStrings('Hello', ' World'):", ConcatenateStrings('Hello', ' World'))  # Expected output: 'Hello World'

# Test EuclideanDistance function
point1 = (1, 2)
point2 = (4, 6)
print("EuclideanDistance((1, 2), (4, 6)):", EuclideanDistance(point1, point2))  # Expected output: 5.0

# Test AppendToList function
list_example = [1, 2, 3]
AppendToList(list_example, 4)
print("AppendToList([1, 2, 3], 4):", list_example)  # Expected output: [1, 2, 3, 4]

# Test CrossProduct function
Vector = namedtuple('Vector', ['i', 'j', 'k'])
v1 = Vector(i=1, j=2, k=3)
v2 = Vector(i=4, j=5, k=6)
cross_product = CrossProduct(v1, v2)
print("CrossProduct((1, 2, 3), (4, 5, 6)):", cross_product)  # Expected output: Vector(i=-3, j=6, k=-3)
