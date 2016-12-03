from binascii import hexlify, unhexlify


class IllegalArgumentError(ValueError):
    pass


def xor_char(c1, c2):
    return chr(ord(c1) ^ ord(c2))


def fixed_xor(s1, s2):
    if len(s1) != len(s2):
        raise IllegalArgumentError("length of strings should be equals")
    s1, s2 = unhexlify(s1), unhexlify(s2)
    return hexlify(''.join(xor_char(a, b) for a, b in zip(s1, s2)))
