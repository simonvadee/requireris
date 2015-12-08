import binascii
import random
import string
import sys
from os import listdir, remove
from getpass import getpass

import reqTOTP
from reqPGP import reqPGP
from reqGUI import reqGUI

class OTPManager(object):
    """
    GENERATE SEED
    STORE SEED IN ENCRYPTED FILES
    MANAGE UI ?
    """

    def __init__(self):
        # ask where accounts will be stored
        self.pgp = reqPGP()
        self.otp = None
        self.session = None
        self.connectTry = 0
        self.gui = reqGUI(self)

    def openExistingSession(self, account, passphrase):
        if account == self.session:
            print("already signed in !")
            return None
        data = str()
        try:
            data = self.pgp.decryptFile(account, passphrase)
            if data == '':
                if self.connectTry < 3:
                    self.connectTry += 1
                    return None
                else:
                    print("3 password errors, exiting now...")
                    sys.exit()
        except FileNotFoundError:
            print("this account does not exist")
            return None
        self.connectTry = 0
        self.session = account
        self.otp = reqTOTP.reqTOTP(data)
        return self.otp.get()

    def createNewSession(self, account, passphrase, confirm_passphrase, secret):
        if account == self.session:
            print("already signed in !")
            return None
        if passphrase != confirm_passphrase:
            print("wrong confirmation passphrase")
            return None
        key = self.pgp.genKey(account, passphrase)
        if secret == '':
            secret = genSeed()
        try:
            self.otp = reqTOTP.reqTOTP(secret)
        except binascii.Error:
            self.pgp.deleteKey(key.fingerprint)
            return None
        self.pgp.encryptFile(account, secret)
        self.session = account
        return self.otp.get()

    def get(self):
        if not self.otp:
            print("no active session")
        else:
            return self.otp.get()


    def listAccounts(self):
        files = [name for name in listdir(self.pgp.path) if name.find('.req') != -1]
        accounts = []
        for filename in files:
            accounts.append(filename[1:filename.find('.req')])
        return accounts
        
    def deleteAccount(self, toDelete):
        keys = self.pgp.gpg.list_keys()
        for key in keys:
            keyName = key['uids'][0][key['uids'][0].find('<') + 1:key['uids'][0].find('>')]
            if keyName == toDelete:
                self.pgp.deleteKey(key['fingerprint'])

        try:
            remove(self.pgp.path + '.' + toDelete + '.req')
        except FileNotFoundError:
            return 'failure'
        return 'success'
        
            
    def updateKey(self, account):
        for index in range(3):
            passphrase = getpass("account's passphrase : ")
            print(passphrase)
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
        secret = input("please enter a 16 bytes secret key (press enter for auto-generation)")
        if secret == '':
            secret = genSeed()
        try:
            self.otp = reqTOTP.reqTOTP(secret)
        except binascii.Error:
            return
        self.pgp.encryptFile(account, secret)
        return self.otp.get()

    def disconnect(self):
        self.otp = None
        self.session = None
    
def genSeed(size=16, source=string.ascii_lowercase):
    seed = ''.join(random.SystemRandom().choice(source) for _ in range(size))
    return seed


def padSeed(seed, padding=8):
    seed = seed.replace(' ', '')
    while len(seed) % padding != 0:
        seed += '='
    return seed
