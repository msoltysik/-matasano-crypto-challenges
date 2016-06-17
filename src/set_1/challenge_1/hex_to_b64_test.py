from unittest import TestCase

from src.set_1.challenge_1.hex_to_b64 import hex_to_b64


class HexToB64Test(TestCase):
    def test_case_1(self):
        given = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        self.assertEqual(expected, hex_to_b64(given))
