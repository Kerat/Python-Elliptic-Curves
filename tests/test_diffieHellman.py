#coding: utf8
from unittest import TestCase
from src.DiffieHellman import *

class TestDiffieHellman(TestCase):
    def test_echange_secret(self):
        alice = DiffieHelman()
        bob = DiffieHelman()
        alice.compute_secret(bob.get_shared_key())
        alice_secret = alice.shared_secret
        bob.compute_secret(alice.get_shared_key())
        bob_secret = bob.shared_secret
        self.assertEqual(alice_secret,bob_secret)
        print(alice_secret)
        print(bob_secret)