from unittest import TestCase

from src.set_1.challenge_1.fixed_xor import fixed_xor, IllegalArgumentError, xor_char


class FixedXORTest(TestCase):
    def test_case_1(self):
        given = 'a', 'a'
        expected = '\x00'

        self.assertEqual(expected, xor_char(*given))

    def test_case_2(self):
        given = '1c0111001f010100061a024b53535009181c', \
                '686974207468652062756c6c277320657965'
        expected = '746865206b696420646f6e277420706c6179'

        self.assertEqual(expected, fixed_xor(*given))

    def test_case_3(self):
        given = '1c0111001f', \
                '686974207468652062756c6c277320657965'

        with self.assertRaises(IllegalArgumentError):
            fixed_xor(*given)
