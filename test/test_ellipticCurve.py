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