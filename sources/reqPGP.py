from gnupg import GPG
from os import environ

class reqPGP(object):

    def __init__(self, path='./accounts/'):
        self.gpg = GPG(gnupghome=environ["HOME"] + "/.reqkeys")
        self.path = path
        
    def genKey(self, account, passphrase):
        input_data = self.gpg.gen_key_input(
            name_email=account,
            passphrase=passphrase)
        key = self.gpg.gen_key(input_data)
        
    def encryptFile(self, account, data):
        encryptedData = str(self.gpg.encrypt(data, account))
        with open(self.path + account + '.req', 'w') as f:
            f.write(encryptedData)
        
    def decryptFile(self, account, passphrase):
        with open(self.path + account + '.req', 'rb') as f:
            decryptedData = str(self.gpg.decrypt_file(f, passphrase=passphrase))
        return decryptedData
