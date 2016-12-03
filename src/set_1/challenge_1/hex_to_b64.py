from base64 import b64encode

from binascii import unhexlify


def hex_to_b64(hex_string):
    byte_seq = unhexlify(hex_string)
    return b64encode(byte_seq)
