#coding: utf8
"""
Authors : MARCE Tarek - GHELIS Amin
Version : 0.1
"""
from unittest import TestCase
from src.DiffieHellman import DiffieHellman


class TestDiffieHellman(TestCase):
    def test_get_shared_key(self):
        alice = DiffieHellman.DiffieHelman()
        self.assertEqual(alice.get_shared_key(),alice.shared_key)

    def test_echange_secret(self):
        alice = DiffieHellman.DiffieHelman()
        bob = DiffieHellman.DiffieHelman()
        alice.compute_secret(bob.get_shared_key())
        alice_secret = alice.shared_secret
        bob.compute_secret(alice.get_shared_key())
        bob_secret = bob.shared_secret
        self.assertEqual(alice_secret,bob_secret)
