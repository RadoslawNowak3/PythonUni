import unittest
from points import *


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(1, 5)

    def test_str(self):
        self.assertEqual(str(self.point), "(1,5)")

    def test_repr(self):
        self.assertEqual(repr(self.point), "Point(1,5)")

    def test_eq(self):
        self.assertTrue(self.point == Point(1, 5))
        self.assertTrue(self.point != Point(4, 5))

    def test_add(self):
        self.assertEqual(self.point + Point(1, 6), Point(2,11))

    def test_sub(self):
        self.assertEqual(self.point - Point(1, 6), Point(0, -1))

    def test_mul(self):
        self.assertEqual(self.point * Point(1, 6), Point(1, 30))

    def test_cross(self):
        self.assertEqual(self.point.cross(Point(1, 2)), -3)

    def test_length(self):
        self.assertEqual(self.point.length(),math.sqrt(26))

    def test_hash(self):
        self.assertEqual(hash(self.point),hash((Point)(1,5)))

    def tearDown(self):
        del self.point


if __name__ == '__main__':
    unittest.main()