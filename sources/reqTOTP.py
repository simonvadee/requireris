from reqHOTP import reqHOTP
from hashlib import sha1
import time as _time

class reqTOTP(reqHOTP):
    """
    """
    
    def __init__(self, secret, sync=30):
        self.sync = sync
        super(reqTOTP, self).__init__(secret)


    def get(self, time=None):
        if not time:
            time = _time.time()
        count = int(time) // self.sync
        return super(reqTOTP, self).get(count)
        
    def check(self, code, time=None):
        return hmac.compare_digest(code, self.get(time))
