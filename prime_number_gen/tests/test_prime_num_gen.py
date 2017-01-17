import unittest

from code.prime_num_gen import prime_num_gen

class TestPrimeNumberGen(unittest.TestCase):
    def test_returns_list(self):  
        # self.assertEqual('bar', Foo().bar())
        self.assertIsInstance(prime_num_gen(3),list)
        
        
if __name__ == '__main__':
	unittest.main()
     
    
    
    
