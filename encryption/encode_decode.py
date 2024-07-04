class Encryption():
    def __init__(self,word,key=50):
        self.key = key
        self.word = word

    def encrypt_decrypt(self):
        secret = ''
        for ch in self.word:
            secret += chr(ord(ch) ^ self.key)
        return secret

encrypt = Encryption("salam")
decrypt = Encryption("AS^S_")
print(encrypt.encrypt_decrypt())
print(decrypt.encrypt_decrypt())

