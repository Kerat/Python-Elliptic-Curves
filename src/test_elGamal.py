from unittest import TestCase
from src.ElGamal import ElGamal

class TestElGamal(TestCase):
    def test_encrypt_decrypt(self):
        alice = ElGamal(True)
        bob = ElGamal(False)
        message = "TEST"
        encrypted_message = bob.encrypt_fake_points(message,alice.get_public_key())
        decrypted_message = alice.decrypt(encrypted_message)
        self.assertEqual(encrypted_message,decrypted_message)
