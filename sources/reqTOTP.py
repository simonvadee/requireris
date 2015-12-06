import binascii
import time as _time
from hmac import compare_digest

from reqHOTP import reqHOTP


class reqTOTP(reqHOTP):
    """
    """

    def __init__(self, secret, sync=30):
        self.sync = sync
        try:
            super(reqTOTP, self).__init__(secret)
        except binascii.Error as e:
            raise e

    def get(self, time=None):
        if not time:
            time = _time.time()
        count = int(time) // self.sync
        return super(reqTOTP, self).get(count)

    def check(self, code, time=None):
        return compare_digest(code, self.get(time))
