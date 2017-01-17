import unittest

from code.prime_num_gen import prime_num_gen

class TestPrimeNumberGen(unittest.TestCase):
	def test_returns_list(self):  
		""" test that the function returns a list"""
		# self.assertEqual('bar', Foo().bar())
		self.assertIsInstance(prime_num_gen(3),list)
	
	def test_not_integer(self):
		with self.assertRaises(TypeError):
			prime_num_gen("hello")
			
	def test_negative_input_return_none(self):
		self.assertEqual(None, prime_num_gen(-3))
		
if __name__ == '__main__':
	unittest.main()
	
	
	

