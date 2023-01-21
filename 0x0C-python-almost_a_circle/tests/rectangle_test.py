import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_creation(self):
        a = Rectangle(3, 4)
        self.assertEqual(a.id, 1)
        b = Rectangle(3, 4)
        self.assertEqual(b.id, 1)
        r3 = Rectangle(10, 2, 0, 0, 12)
        print(r3.id)
    
    def test_