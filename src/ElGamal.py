#!/usr/bin/env python3
# coding: utf8

from .EllipticCurve import EllipticCurve
from secrets import randbelow


class ElGamal:
    def __init__(self, is_alice):
        self.p = int("F1FD178C0B3AD58F10126DE8CE42435B3961ADBCABC8CA6DE8FCF353D86E9C03", 16)
        self.A = int("F1FD178C0B3AD58F10126DE8CE42435B3961ADBCABC8CA6DE8FCF353D86E9C00", 16)
        self.B = int("EE353FCA5428A9300D4ABA754A44C00FDFEC0C9AE4B1A1803075ED967B7BB73F", 16)
        self.P = (int("B6B3D4C356C139EB31183D4749D423958C27D2DCAF98B70164C97A2DD98F5CFF", 16),
                  int("6142E0F7C8B204911F9271F0F3ECEF8C2701C307E8E4C9E183115A1554062CFB", 16),
                  0)
        self.q = int("F1FD178C0B3AD58F10126DE8CE42435B53DC67E140D2BF941FFDD459C6D655E1", 16)
        self.i = 1
        self.ec = EllipticCurve(self.A, self.B, self.P, self.p)
        if is_alice:
            self.alice = True
            self.private_key = randbelow(self.q - 2) + 1
            self.public_key = self.ec.multiply(self.P, self.private_key)

    def get_public_key(self):
        if self.alice:
            return self.public_key
        else:
            raise Exception("Cannot give a public key ! I am not alice !")

    def encrypt_fake_points(self, message, pub_key):
        message_points = self.message_to_points_fake(message)
        random_number = randbelow(self.q - 1) + 1
        encrypted_couples = []
        for e in message_points:
            c1 = self.ec.multiply(self.P, random_number)
            c2 = self.ec.sum(e, self.ec.multiply(pub_key, random_number))
            encrypted_couples.append((c1, c2))
        return encrypted_couples

    def encrypt_points(self, message, pub_key):
        message_points = self.message_to_points(message)
        random_number = randbelow(self.q - 1) + 1
        encrypted_couples = []
        for e in message_points:
            c1 = self.ec.multiply(self.P, random_number)
            c2 = self.ec.sum(e, self.ec.multiply(pub_key, random_number))
            encrypted_couples.append((c1, c2))
        return encrypted_couples

    def message_to_points_fake(self, message):
        list_message = []
        for c in message:
            list_message.append(self.ec.multiply(self.P, ord(c)))
        return list_message

    def message_to_points(self, message):
        list_message = []
        for c in message:
            list_message.append(self.ec.compute_y(ord(c)))
        return list_message

    def decrypt(self, encrypted_couples):
        decrypted_list = []
        for e in encrypted_couples:
            dac1 = self.ec.multiply(e[0], self.private_key)
            decrypted_list.append(self.ec.sum(e[1], self.ec.opposite(dac1)))
        return decrypted_list


def points_to_message(points):
    string = ""
    for p in points:
        string = string + chr(p[0])
    return string
