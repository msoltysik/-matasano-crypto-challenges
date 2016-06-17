from base64 import b64encode


def hex_to_b64(hex_string):
    # WARM UP! TODO: rewrite without using base64 library
    return b64encode(hex_string.decode("hex"))
