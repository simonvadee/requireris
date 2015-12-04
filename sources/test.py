import reqTOTP
import reqUtils
import pyotp

seed = reqUtils.OTPManager.genSeed()

testReal = pyotp.TOTP(seed)
testMe = reqTOTP.reqTOTP(seed)

# for i in range(896):
    # if not testMe.check(testReal.now(), i):
print('---->', testReal.now(), '====', testMe.get())
