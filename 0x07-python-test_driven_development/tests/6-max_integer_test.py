#!/usr/bin/python3
import unittest

class TestMaxInteger(unittest.TestCase):
    
    def test_normal_execution(self):
        test_list = [1, 2, 3, 5, -10]
        self.assertEqual(max_integer(test_list), 5)

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)
        
    def test_one_element(self):
        one_element = [500]
        self.assertEqual(max_integer(one_element), 500)

    def test_bigger_first(self):
        bigger_first = [100, 10]
        self.assertEqual(max_integer(bigger_first), 100)

    def test_negative_numbers(self):
        negative = [-20, -10, -15]
        self.assertEqual(max_integer(negative), -10)

    def test_duplicates(self):
        duplicates = [2, 2, 2]
        self.assertEqual(max_integer(duplicates), 2)

    def test_mixed_list(self):
        mixed_list = [1, "hello", [], -2]
        with self.assertRaises(TypeError):
            max_integer(mixed_list)
            
if __name__ == '__main__': 
    unittest.main()