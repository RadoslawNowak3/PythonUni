from Stack import *
import unittest


class Test(unittest.TestCase):
  def setUp(self):
    self.stack = Stack();

  def test_str(self):
    self.assertEqual(str(self.stack), '[]')

  def test_eq(self):
    self.assertEqual(self.stack, Stack())

  def test_is_empty(self):
    self.assertEqual(self.stack.is_empty(), True)

  def test_is_full(self):
    self.assertEqual(self.stack.is_full(), False)

  def test_pop(self):
    self.stack.push(10)
    self.stack.push(20)
    self.assertEqual(self.stack.pop(), 20)

  def test_push(self):
    self.stack.push(5)
    self.stack.push(4)
    self.stack.push(3)
    self.assertEqual(self.stack, Stack([5, 4, 3]))
  def tearDown(self): pass

if __name__ == '__main__':
  unittest.main()