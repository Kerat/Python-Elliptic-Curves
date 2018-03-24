# coding: utf8
from EllipticCurve import EllipticCurve
from secrets import randbelow


class DiffieHellman:
    def __init__(self):
        self.p = int("F1FD178C0B3AD58F10126DE8CE42435B3961ADBCABC8CA6DE8FCF353D86E9C03", 16)
        self.A = int("F1FD178C0B3AD58F10126DE8CE42435B3961ADBCABC8CA6DE8FCF353D86E9C00", 16)
        self.B = int("EE353FCA5428A9300D4ABA754A44C00FDFEC0C9AE4B1A1803075ED967B7BB73F", 16)
        self.P = (int("B6B3D4C356C139EB31183D4749D423958C27D2DCAF98B70164C97A2DD98F5CFF", 16),
                  int("6142E0F7C8B204911F9271F0F3ECEF8C2701C307E8E4C9E183115A1554062CFB", 16),
                  0)
        self.q = int("F1FD178C0B3AD58F10126DE8CE42435B53DC67E140D2BF941FFDD459C6D655E1", 16)
        self.i = 1
        self.ec = EllipticCurve(self.A, self.B, self.P, self.p)
        self.pre_key = randbelow(self.q - 1)
        self.shared_key = self.ec.multiply(self.P, self.pre_key)
        self.shared_secret = (0, 0, 1)

    def compute_secret(self, foreign):
        secret = self.ec.multiply(foreign, self.pre_key)
        self.shared_secret = secret

    def get_shared_key(self):
        return self.shared_key
