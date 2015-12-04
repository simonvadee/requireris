from base64 import b32encode
import random
import string

class OTPManager(object):
    """
    GENRATE SEED
    STORE SEED IN ENCRYPTED FILES
    MANAGE UI ?
    """
    
    @staticmethod
    def genSeed(size=16, source=string.ascii_lowercase):
        seed = ''.join(random.SystemRandom().choice(source) for char in range(size))
        return seed

    @staticmethod
    def padSeed(seed, padding=8):
        if len(seed) % padding != 0:
            seed = seed.ljust(8, '=')
        return seed
