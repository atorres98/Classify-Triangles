import unittest
def classify_triangles(a, b, c): #function to define the types of triangles
	if a == b == c:
		return 'Equilateral'
	elif a == b != c:
		return 'Isosceles'
	elif a != b != c:
		if c**2 == b**2 + a**2:
			return 'Right'
		return 'Scalene'

#print the outcome of the above function
def run_classify_triangles(a, b, c):
	print(classify_triangles(a,b,c))