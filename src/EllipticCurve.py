#!/usr/bin/env python3
# coding=utf-8
from math import sqrt
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
                "The given point " + str(point) + " is not on the curve with coefficients a = " + str(self.a) +
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
        if type(point[0]) is not int:
            raise Exception("The type of the points coordinates must be integer")
        x = point[0]
        y = point[1]
        test = x ** 3 + self.a * x + self.b
        test = test % self.modulo
        if test == (y ** 2 % self.modulo):
            return True
        else:
            return False

    def compute_y(self,x):
        """
        Return the y of a point on the curve for a given x.
        :param x: The x of the point we are looking for.
        :return: The y of the point we are looking for.
        """
        y_2 = (x ** 3 + self.a * x + self.b)%self.modulo
        return y_2 ** (self.modulo+1/2)

    def sum(self, point1, point2):
        """
        Compute the sum of two points.
        :param point1: First point to sum (a 3 elements tuple).
        :param point2: Second point to sum (a 3 elements tuple).
        :return: The result point of the sum (a 3 elements tuple).
        """
        if not self.point_check(point1) or not self.point_check(point2):
            raise Exception("One or the two given points do not belong to the curve !")
        if point1[2] == 1:
            return point2
        if point2[2] == 1:
            return point1
        if point1[0] == point2[0] and point1[1] == point2[1]:
            return self.double(point1)
        if point1[0] == point2[0]:
            return 0, 0, 1
        lambda_1 = point2[1] - point1[1]
        lambda_2 = point2[0] - point1[0]
        llambda = (lambda_1 * self.inv_modulo(lambda_2, self.modulo)) % self.modulo
        x3 = (llambda ** 2) % self.modulo - point1[0] - point2[0]
        x3 = x3 % self.modulo
        y3 = llambda * (point1[0] - x3) - point1[1]
        y3 = y3 % self.modulo
        return x3, y3, 0

    def double(self, point):
        """
        Compute the double of a point (multiply it by two).
        :param point: The point to double (a 3 elements tuple).
        :return: The double of the point given in parameter (a 3 elements tuple).
        """
        if not self.point_check(point):
            raise Exception("The given point do not belong to the curve !")
        if point[1] == 0 or point[2] == 1:
            return 0, 0, 1
        lambda_1 = 3 * point[0] ** 2 + self.a
        lambda_2 = 2 * point[1]
        llambda = (lambda_1 * self.inv_modulo(lambda_2, self.modulo)) % self.modulo
        x3 = (llambda ** 2) % self.modulo - (2 * point[0]) % self.modulo
        y3 = llambda * (point[0] - x3) - point[1]
        y3 = y3 % self.modulo
        return x3, y3, 0

    def opposite(self, point):
        """
        Compute the opposite of a point
        :param point: The point to treat (a 3 elements tuple).
        :return: The opposite of the point given in parameter (a 3 elements tuple).
        """
        if not self.point_check(point):
            raise Exception("The given point do not belong to the curve !")
        # Demander au prof ce qu'il est censé se passer avec le point à l'infini
        if point[2] == 1:
            return point
        return point[0], -point[1], 0

    def multiply(self, point, n):
        """
        Multiply by n a given point.
        :param point: The point to multiply (a 3 elements tuple).
        :param n: The factor of the multiplication (an integer)
        :return: The result point of the multiplication (a 3 elements tuple).
        """
        if not self.point_check(point):
            raise Exception("The given point do not belong to the curve !")
        p = (point[0], point[1], 1)
        if n == 0:
            return p
        if n < 0:
            _n = -n
            q = self.opposite(point)
        else:
            _n = n
            q = point
        while _n != 0:
            if _n % 2 != 0:
                p = self.sum(p, q)
            _n = int(_n / 2.)
            if _n == 0:
                break
            else:
                q = self.double(q)
        return p

    def bezout(self, a, b):
        """
        Return (u, v, p) of the equation : a*u + b*v = p.
        p is the gcd of a and b.
        :param a: First parameter.
        :param b: Second parameter.
        :return: (u, v, p).
        """
        if a == 0 and b == 0:
            return 0, 0, 0
        if b == 0:
            return int(a / abs(a)), 0, abs(a)
        (u, v, p) = self.bezout(b, a % b)
        return v, (u - v * int(a / b)), p

    def inv_modulo(self, x, m):
        """
        Return the symmetric of x modulo m
        :param x: parameter wich we want to find the symmetric.
        :param m: modulo in wich the symmetric will be calculate.
        :return: Return the symmetric, raise an exception if the numbers are not primes between each other.
        """
        (u, _, p) = self.bezout(x, m)
        if p == 1:
            return u % abs(m)
        else:
            raise Exception("%s and %s are not primes between each other." % (x, m))
