import unittest
from ClassifyTriangles import classify_triangles
from ClassifyTriangles import run_classify_triangles


class test_triangles(unittest.TestCase):
	def testSet1(self): #test all four types of triangles
		self.assertEqual(classify_triangles(3,4,5),'Right', '3, 4, 5 is a right triangle')
		self.assertEqual(classify_triangles(6,6,2), 'Isosceles', '6, 6, 2 is an isosceles triangle')
		self.assertEqual(classify_triangles(1,3,5), 'Scalene', '1, 3, 5 is a scalene triangle')
		self.assertEqual(classify_triangles(2, 2, 2), 'Equilateral', '2, 2, 2 is an equilateral triangle')
	
	def testSet2(self): #test only equilateral triangles
		self.assertEqual(classify_triangles(20,20,20), 'Equilateral', '20, 20, 20 is an equilateral triangle')
		self.assertEqual(classify_triangles(9,9,9), 'Equilateral', '9, 9, 9 is an equilateral triangle')
		self.assertEqual(classify_triangles(8,8,8),'Equilateral', '8,8,8 is an equilateral triangle')
	
	def testSet3(self): #test only scalene triangles
		self.assertEqual(classify_triangles(2, 8, 5), 'Scalene', '2, 8, 5 is a scalene triangle')
		self.assertEqual(classify_triangles(13, 6, 4), 'Scalene', '13, 6, 4 is a scalene triangle')
		self.assertEqual(classify_triangles(7, 3, 1), 'Scalene', '7, 3, 1 is a scalene triangle')
	
	def testSet4(self): #test only isosceles triangles
		self.assertEqual(classify_triangles(2, 2, 4), 'Isosceles', '2, 2, 4 is an isosceles triangle')
		self.assertEqual(classify_triangles(11, 13, 11), 'Isosceles', '11, 13, 11 is an isosceles triangle')
		self.assertEqual(classify_triangles(45, 45, 7), 'Isosceles', '45, 45, 7 is an isosceles triangle')
	
	def testSet5(self): #test only right triangles
		self.assertEqual(classify_triangles(8, 15, 17), 'Right', '8, 15, 17 is a right triangle')
		self.assertEqual(classify_triangles(5, 12, 13), 'Right', '5, 12, 13 is a right triangle')
		self.assertEqual(classify_triangles(7, 24, 25), 'Right', '7, 24, 25 is a right triangle')

#run the code
if __name__=='__main__':
	run_classify_triangles(5, 6, 7)
	run_classify_triangles(9, 9, 9)
	run_classify_triangles(8, 15, 17)
	run_classify_triangles(2, 2, 4)

	unittest.main(exit=False)