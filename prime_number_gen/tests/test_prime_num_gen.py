import unittest

from code.prime_num_gen import prime_num_gen

class TestPrimeNumberGen(unittest.TestCase):
	def test_returns_list(self):  
		""" test that the function returns a list if input is positive integer"""
		# self.assertEqual('bar', Foo().bar())
		self.assertIsInstance(prime_num_gen(3),list)
	
	def test_not_integer(self):
		with self.assertRaises(TypeError):
			prime_num_gen("hello")
			
	def test_negative_input_return_none(self):
		self.assertEqual(None, prime_num_gen(-3))
		
	def test_returns_correct_output_1(self):
		self.assertEqual([2,3,5,7], prime_num_gen(7))
		
	def test_returns_correct_output_for_2(self):
		# 1 is not a prime number, but two is even if it's even
		self.assertEqual([2], prime_num_gen(2))
		
	def test_returns_correct_output_for_0(self):
		# should return an empty list
		self.assertEqual([], prime_num_gen(0))
	
	def test_returns_correct_output_for_1(self):
		# should return an empty list
		self.assertEqual([], prime_num_gen(1))
		
if __name__ == '__main__':
	unittest.main()
	
	
	

