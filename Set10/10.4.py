from Queue import *
import unittest


class Test(unittest.TestCase):
  def setUp(self):
    self.queue = Queue();

  def test_str(self):
    self.assertEqual(str(self.queue), '[None, None, None, None, None, None]')

  def test_eq(self):
    self.assertEqual(self.queue, Queue())

  def test_is_empty(self):
    self.assertEqual(self.queue.is_empty(), True)

  def test_is_full(self):
    self.assertEqual(self.queue.is_full(), False)

  def test_get(self):
    self.queue.put(20)
    self.assertEqual(self.queue.get(), 20)

  def test_put(self):
    self.queue.put(5)
    self.queue.put(4)
    self.queue.put(3)
    self.assertEqual(self.queue, Queue([5, 4, 3]))
  def tearDown(self): pass

if __name__ == '__main__':
  unittest.main()