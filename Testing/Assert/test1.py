# to run all the test, you need to run the following commands
# You can run 
# This below command will automatically locate your test file and run all the test
# 1) python -m unittest 
# or to be more specific to run all the tests,
# 2) python -m unittest discover -p *test1.py

import unittest

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime"""
        self.assertFalse(is_prime(1))
    
    def test_2(self):
        """Check that 2 is prime"""
        self.assertTrue(is_prime(2))
    
    def test_8(self):
        """Check that 8 is not prime"""
        self.assertFalse(is_prime(8))
    
    def test_11(self):
        """Check that 11 is a prime"""
        self.assertTrue(is_prime(11))
    
    def test_25(self):
        """Check that 25 is not a prime"""
        self.assertFalse(is_prime(25))
    
    def test_28(self):
        """Check that 28 is not a prime"""
        self.assertFalse(is_prime(28))
    
    if __name__ == "__main__":
        unittest.main()