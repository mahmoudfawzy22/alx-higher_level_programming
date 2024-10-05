#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def __init__(self, matrix):
        self.matrix = matrix
    
    def TestOne(self):
        self.assertEqual(max([3, 4, 5, 6 , 8]), 8)
    
    def TestTwo(self):
        self.assertEqual(max([4, 3, 2, 2]), 4)
    
    def TestThree(self):
        self.assertEqual(max([-1, -2, -3]), -1)
    
    def TestFour(self):
        self.assertEqual(max([98]), 98)
        
if __name__ == '__main__':
    unittest.main()