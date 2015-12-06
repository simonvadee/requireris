import binascii
import random
import string
import sys
from getpass import getpass

from reqPGP import reqPGP
from reqTOTP import reqTOTP


class OTPManager(object):
    """
    GENERATE SEED
    STORE SEED IN ENCRYPTED FILES
    MANAGE UI ?
    """

    def __init__(self):
        self.pgp = reqPGP()
        self.otp = None
        self.session = None

    def openExistingSession(self):
        account = input("account's name : ")
        if account == self.session:
            print("already signed in !")
            return
        data = str()
        for index in range(3):
            passphrase = getpass("account's passphrase : ")
            try:
                data = self.pgp.decryptFile(account, passphrase)
                if data != '':
                    break
            except FileNotFoundError:
                print("this account does not exist")
                return
        if data == '':
            print("3 password errors, exiting now...")
            sys.exit()
        self.session = account
        self.otp = reqTOTP(data)
        return self.otp.get()

    def createNewSession(self):
        account = input("new account's name : ")
        passphrase = getpass("new account's passphrase : ")
        confirm_passphrase = getpass("confirm new account's passphrase : ")
        if passphrase != confirm_passphrase:
            print("wrong confirmation passphrase")
            return
        self.pgp.genKey(account, passphrase)
        secret = input("please enter a 16 bytes secret key (press enter for auto-generation)")
        if secret == '':
            secret = genSeed()
        try:
            self.otp = reqTOTP(secret)
        except binascii.Error:
            # delete key
            return
        self.pgp.encryptFile(account, secret)
        return self.otp.get()

    def get(self):
        if not self.otp:
            print("no active session")
        else:
            return self.otp.get()


def genSeed(size=16, source=string.ascii_lowercase):
    seed = ''.join(random.SystemRandom().choice(source) for _ in range(size))
    return seed


def padSeed(seed, padding=8):
    seed = seed.replace(' ', '')
    while len(seed) % padding != 0:
        seed += '='
    return seed
