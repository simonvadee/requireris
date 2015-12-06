import base64
import binascii
import hmac
import struct
from hashlib import sha1

import reqUtils


class reqHOTP(object):
    """
    """

    def __init__(self, secret, digits=6, hashfunc=sha1):
        try:
            self.secret = base64.b32decode(reqUtils.padSeed(secret), casefold=True)
        except binascii.Error as e:
            print(e)
            raise e
        self.digits = digits
        self.hashfunc = hashfunc

    def get(self, count):
        count = bytes(bytearray(struct.pack('>Q', count)))
        digest = hmac.new(self.secret, count, self.hashfunc).digest()
        offset = digest[-1] & 0xf
        byte = struct.unpack(">I", digest[offset:offset + 4])[0]
        byte &= 0x7fffffff
        code = str(byte % (10 ** self.digits))
        code = code.rjust(6, '0')
        return code

    def check(self, code, count):
        return hmac.compare_digest(code, self.get(count))
        pass
