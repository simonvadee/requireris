from reqHOTP import reqHOTP
from hashlib import sha1
import time as _time
import datetime

class reqTOTP(reqHOTP):
    """
    """
    
    def __init__(self, secret, sync=30):
        """
        """

        self.sync = sync
        super(reqTOTP, self).__init__(secret)


    def get(self, time=None):
        if not time:
            time = int(_time.mktime(datetime.datetime.now().timetuple()) // self.sync)
        return super(reqTOTP, self).get(time)
        
    def check(self, code, time):
        pass
