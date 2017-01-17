import unittest

from code.prime_num_gen import prime_num_gen

class TestPrimeNumberGen(unittest.TestCase):
	def test_returns_list(self):  
		""" test that the function returns a list if input is positive integer """
		# self.assertEqual('bar', Foo().bar())
		self.assertIsInstance(prime_num_gen(3),list)
	
	def test_not_integer(self):
		""" test that the function raises a TypeError if input is not an integer """
		with self.assertRaises(TypeError):
			prime_num_gen({})
			
	def test_negative_input_return_none(self):
		""" test that the function returns None if input is a negative number """
		self.assertEqual(None, prime_num_gen(-3))
		
	def test_returns_correct_output_1(self):
		""" test that the function returns the correct output """
		self.assertEqual([2,3,5,7], prime_num_gen(7))
		
	def test_returns_correct_output_for_2(self):
		""" test that the function returns [2] if input is 2 """
		# 1 is not a prime number, but two is, even if it's even
		self.assertEqual([2], prime_num_gen(2))
		
	def test_returns_correct_output_for_0(self):
		""" test that the function returns an empty list if input is zero """
		self.assertEqual([], prime_num_gen(0))
	
	def test_returns_correct_output_for_1(self):
		""" test that the function returns None if input is 1 """
		self.assertEqual([], prime_num_gen(1))
		
	def test_not_input_exists_if_variable(self):
		""" test that the function raises a Name Error if input is undefined """
		with self.assertRaises(NameError):
			prime_num_gen(x_num)
			
	def test_input_string_raise_error(self):
		""" test that the function raises a TypeError if input is a string """
		with self.assertRaises(TypeError):
			prime_num_gen("hello")
			
	def test_input_float_raise_error(self):
		""" test that the function raises a TypeError if input is a float """
		with self.assertRaises(TypeError):
			prime_num_gen(3.4)
			
	def test_input_list_raise_error(self):
		""" test that the function raises a TypeError if input is a list """
		with self.assertRaises(TypeError):
			prime_num_gen([4,"yay"])
		
	
		
if __name__ == '__main__':
	unittest.main()
	
	
	

