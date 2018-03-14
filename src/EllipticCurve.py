from builtins import Exception


class EllipticCurve:
    def __init__(self, a, b, point, modulo):
        """
        Constructor of the EllipticCurve class
        :param a: First coefficient of the curve
        :param b: Second coefficient of the curve
        :param point: A point that is on the curve
        :param modulo: Modulo used for elliptic curve cryptography operations
        """
        self.a = a
        self.b = b
        self.modulo = modulo
        if self.point_check(point):
            self.point = point
        else:
            raise Exception(
                "The given point " + str(point) + " is not on the curve with coeficients a = " + str(self.a) +
                " b = " + str(self.b))

    def point_check(self, point):
        """
        Testing if the given point is on the curve
        :param point: point to test (it's a tuple of integers)
        :return: True if the given point is on the curve, False otherwise
        """
        if len(point) != 3:
            return False
        if point[2] == 1:
            return True
        x = point[0]
        y = point[1]
        test = x ** 3 + self.a * x + self.b
        test = test % self.modulo
        if test == y ** 2:
            return True
        else:
            return False
