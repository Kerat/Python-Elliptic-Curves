from unittest import TestCase

from src.EllipticCurve import EllipticCurve


class TestEllipticCurve(TestCase):
    def test_point_check(self):
        point = (7, 4, 0)
        a = 1
        b = 3
        mod = 17
        with self.assertRaises(Exception):
            EllipticCurve(a, b, point, mod)

        point = (3, 4, 0)
        EllipticCurve(a, b, point, mod)

        point = (0, 0, 1)
        EllipticCurve(a, b, point, mod)

    def test_sum(self):
        # Test non valid values : float
        # Test non valid values : str
        # Test a point not on the curve.
        # Test 'the infinite point'
        # Test correct with x1 != x2
        # Test correct with x1 == x2
        # Test uncorrect with x1 != x2
        # Test uncorrect with x1 == x2
        return None

    def test_double(self):
        # Test non valid values : float
        # Test non valid values : str
        # Test a point not on the curve.
        # Test 'the infinite point'
        # Test correct with y1 != 0
        # Test correct with y1 == 0
        # Test uncorrect with y1 != 0
        # Test uncorrect with y1 == 0
        return None

    def test_opposite(self):
        # Test non valid values : float
        # Test non valid values : str
        # Test a point not on the curve.
        # Test 'the infinite point'
        # Test correct 1
        # Test correct 2
        # Test uncorrect 1
        # Test uncorrect 2
        return None

    def test_multiply(self):
        # Test non valid values : float
        # Test non valid values : str
        # Test n=0
        # Test a point not on the curve.
        # Test 'the infinite point'
        # Test correct 1
        # Test correct 2
        # Test uncorrect
        return None