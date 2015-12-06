from os import name as osName, environ

from gnupg import GPG


class reqPGP(object):
    def __init__(self, path=None):
        self.gpg = GPG(gpgbinary=('gpg.exe' if osName == 'nt' else 'gpg'))
        if not path:
            try:
                self.path = environ["HOME"] + "/.reqAccounts_"
            except KeyError:
                self.path = environ["HOMEPATH"] + "\\.reqAccounts_"
        else:
            if path[-1] != '\\' and osName == 'nt':
                path += '\\'
            elif path[-1] != '/' and osName == 'posix':
                path += '/'
            self.path = path
            

    def genKey(self, account, passphrase):
        input_data = self.gpg.gen_key_input(
            name_email=account,
            passphrase=passphrase)
        self.gpg.gen_key(input_data)

    def encryptFile(self, account, data):
        encryptedData = str(self.gpg.encrypt(data, account))
        with open(self.path + account + '.req', 'w') as f:
            f.write(encryptedData)

    def decryptFile(self, account, passphrase):
        with open(self.path + account + '.req', 'rb') as f:
            decryptedData = str(self.gpg.decrypt_file(f, passphrase=passphrase))
        return decryptedData
