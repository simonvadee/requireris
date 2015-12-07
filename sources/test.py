import reqUtils

test = reqUtils.OTPManager()
print("< list accounts >", test.listAccounts())
test.updateKey('simon')
