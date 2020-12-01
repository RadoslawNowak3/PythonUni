from circles import *
import unittest
class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(0, 0, 6)

    def test_repr(self):
        self.assertEqual(repr(self.circle), "Circle(0,0,6)")


    def test_eq(self):
        self.assertTrue(self.circle == Circle(0, 0, 6))
        self.assertTrue(self.circle != Circle(1, 2, 3))


    def test_area(self):
        self.assertEqual(Circle.area(self.circle), math.pi*36)

    def test_move(self):
        self.assertEqual(Circle.move(self.circle,1,2),Circle(1,2,6))
    def test_cover(self):
        self.assertEqual(Circle.cover(self.circle,Circle(0,0,7)),Circle(0,0,7))
        self.assertEqual(Circle.cover(self.circle, Circle(3, 0, 7)), Circle(2, 0, 8))

    def tearDown(self):
        del self.circle

if __name__ == '__main__':
    unittest.main()
