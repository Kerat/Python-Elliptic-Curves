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

    def sum(self, point1, point2):
        """
        Compute the sum of two points.
        :param point1: First point to sum (a 3 elements tuple).
        :param point2: Second point to sum (a 3 elements tuple).
        :return: The result point of the sum (a 3 elements tuple).
        """
        return (1,2,0)

    def double(self, point):
        """
        Compute the double of a point (multiply it by two).
        :param point: The point to double (a 3 elements tuple).
        :return: The result of the operation
        """
        return (1,2,0)

    def opposite(self, point):
        return (1,2,0)

    def multiply(self, point, n):
        return (1,2,0)