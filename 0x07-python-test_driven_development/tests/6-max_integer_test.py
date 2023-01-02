#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, [3.5])
        self.assertRaises(TypeError, max_integer, ["hello"])
        self.assertRaises(TypeError, max_integer, [TestMaxInteger()])
        self.assertRaises(TypeError, max_integer, [True])
