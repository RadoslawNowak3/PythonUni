from rectangles import *
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(0, 0, 4, 6)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "(0,0,4,6)")

    def test_repr(self):
        self.assertEqual(repr(self.rectangle), "Rectangle(0,0,4,6)")

    def test_eq(self):
        self.assertTrue(self.rectangle == Rectangle(0, 0, 4, 6))
        self.assertTrue(self.rectangle == Rectangle(4, 6, 0, 0))
        self.assertTrue(self.rectangle != Rectangle(1, 2, 3, 4))

    def test_center(self):
        self.assertTrue(Rectangle.center(self.rectangle), Point(2, 3))

    def test_area(self):
        self.assertEqual(Rectangle.area(self.rectangle), 24)

    def test_move(self):
        self.assertEqual(Rectangle.move(self.rectangle, 2, 4), Rectangle(2, 4, 6, 10))
        self.assertEqual(Rectangle.move(self.rectangle, -2, 5), Rectangle(-2, 5, 2, 11))

    def tearDown(self):
        del self.rectangle


if __name__ == '__main__':
    unittest.main()