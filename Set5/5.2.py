import unittest
import fracs

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([6, 6], [2, 4]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 3], [1, 4]), [1, 12])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 4], [6, 3]), [1, 8])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([-3, 5]), False)
        self.assertEqual(fracs.is_positive([1, -5]), False)
        self.assertEqual(fracs.is_positive([-2, -7]), True)
        self.assertEqual(fracs.is_positive([1, 5]), True)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero(self.zero), True)
        self.assertEqual(fracs.is_zero([0, -25]), True)
        self.assertEqual(fracs.is_zero([1, -5]), False)
        self.assertEqual(fracs.is_zero([2, -3]), False)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([3,4],[3,4]),0)
        self.assertEqual(fracs.cmp_frac([2,4],[1,2]),0)
        self.assertEqual(fracs.cmp_frac([1,4],[1,12]),1)
        self.assertEqual(fracs.cmp_frac([1,8],[1,2]),-1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([5,2]), [5.0, 2.0])

    def tearDown(self):
        self.zero = None


if __name__ == '__main__':
    unittest.main()
