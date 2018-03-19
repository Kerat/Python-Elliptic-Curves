# Run test with :
# python3 -m unittest test_ellipticCurve.py

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
            EllipticCurve(1, 3, (3, 4, 0), 17).sum((6.2, 2.5, 0), (2.3, 8.4, 0))
        # Test non valid values : str
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).sum(("str", "str", 0), ("str", "str", 0))
        # Test a point not on the curve.
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).sum((7, 4, 0), (2, 8, 0))
        # Test 2 equals points.
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).sum((3, 4, 0), (3, 4, 0))
        # Test 'the infinite point'
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((6, 2, 0), (2, 8, 1)), (6, 2, 0))
        # Test 'the infinite point' 2
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((6, 2, 1), (2, 8, 0)), (2, 8, 0))
        # Test 'the infinite point' 3
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((6, 2, 1), (2, 8, 1))[2], 0)
        # Test correct with x1 != x2
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((6, 2, 0), (2, 8, 0)), (7, 8, 0))
        # Test correct with x1 == x2
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((3, 4, 0), (3, 13, 0))[2], 1)
        # Test uncorrect with x1 != x2
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((6, 2, 0), (2, 8, 0)), (3, 4, 0))
        # Test uncorrect with x1 == x2
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).sum((3, 4, 0), (3, 13, 0))[2], 0)

    def test_double(self):
        # Test non valid values : float
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).double((6.2, 2.5, 0))
        # Test non valid values : str
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).double(("str", "str", 0))
        # Test a point not on the curve.
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).double((7, 4, 0))
        # Test 'the infinite point'
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).double((2, 8, 1)), (2, 8, 1))
        # Test correct with y1 != 0
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).double((3, 4, 0)), (2, 8, 0))
        # Test correct with y1 == 0
        self.assertEqual(EllipticCurve(1, 1, (2, 1, 0), 3).double((1, 0, 0))[2], 1)
        # Test uncorrect with y1 != 0
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).double((3, 4, 0)), (3, 8, 0))
        # Test uncorrect with y1 == 0
        self.assertNotEqual(EllipticCurve(1, 1, (2, 1, 0), 3).double((1, 0, 0))[2], 0)

    def test_opposite(self):
        # Test non valid values : float
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).opposite((6.2, 2.5, 0))
        # Test non valid values : str
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).opposite(("str", "str", 0))
        # Test a point not on the curve.
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).opposite((7, 4, 0))
        # Test 'the infinite point'
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).opposite((2, 8, 1))[2], 1)
        # Test correct 1
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).opposite((3, 4, 0)), (3, -4, 0))
        # Test correct 2
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).opposite((6, 2, 0)), (6, -2, 0))
        # Test uncorrect 1
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).opposite((3, 4, 0)), (-3, 4, 0))
        # Test uncorrect 2
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).opposite((6, 2, 0)), (6, 2, 0))

    def test_multiply(self):
        # Test non valid values : float
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).multiply((6.2, 2.5, 0), 5)
        # Test non valid values : str
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).multiply(("str", "str", 0), 5)
        # Test n=0
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).multiply((3, 4, 0), 0)
        # Test a point not on the curve.
        with self.assertRaises(Exception):
            EllipticCurve(1, 3, (3, 4, 0), 17).multiply((7, 4, 0), 5)
        # Test 'the infinite point'
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).multiply((2, 8, 1), 5)[2], 1)
        # Test correct 1
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).multiply((3, 4, 0), 3), (11, 7, 0))
        # Test with sum
        ec = EllipticCurve(1, 3, (3, 4, 0), 17)
        s = ec.double((3, 4, 0))
        for i in range(3):
            s = s + ec.sum(s, (3, 4, 0))
        self.assertEqual(ec.multiply((3, 4, 0), 5), s)
        # Test multiplication by same value than modulo, should return infinite
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).multiply((3, 4, 0), 17)[2], 1)
        # Test multiplication by same value than modulo + one, should return the same point
        self.assertEqual(EllipticCurve(1, 3, (3, 4, 0), 17).multiply((3, 4, 0), 17), (3, 4, 0))
        # Test uncorrect
        self.assertNotEqual(EllipticCurve(1, 3, (3, 4, 0), 17).multiply((3, 4, 0), 3), (11, 8, 0))
