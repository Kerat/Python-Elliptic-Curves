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
        with self.assertRaises(Exception):
            EllipticCurve(1,3,(3,4,0),17).sum((6.2,2.5,0),(2.3,8.4,0))
        # Test non valid values : str
        with self.assertRaises(Exception):
            EllipticCurve(1,3,(3,4,0),17).sum(("str","str",0),("str","str",0))
        # Test a point not on the curve.
        with self.assertRaises(Exception):
            EllipticCurve(1,3,(3,4,0),17).sum((7,4,0),(2,8,0))
        # Test 'the infinite point'
        self.assertEqual(EllipticCurve(1,3,(3,4,0),17).sum((6,2,0),(2,8,1)),(6,2,0))
        # Test correct with x1 != x2
        self.assertEqual(EllipticCurve(1,3,(3,4,0),17).sum((6,2,0),(2,8,0)),(7,8,0))
        # Test correct with x1 == x2
        # Test uncorrect with x1 != x2
        self.assertEqual(EllipticCurve(1,3,(3,4,0),17).sum((6,2,0),(2,8,0)),(3,4,0))
        # Test uncorrect with x1 == x2
        return None

    def test_double(self):
        # Test non valid values : float
        # Test non valid values : str
        # Test a point not on the curve.
        # Test 'the infinite point'
        # Test correct with y1 != 0
        self.assertEqual(EllipticCurve(1,3,(3,4,0),17).double((3,4,0)),(2,8,0))
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
        self.assertEqual(EllipticCurve(1,3,(3,4,0),17).opposite((3,4,0)),(3,-4,0))
        # Test correct 2
        self.assertEqual(EllipticCurve(1,3,(3,4,0),17).opposite((6,2,0)),(6,-2,0))
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
