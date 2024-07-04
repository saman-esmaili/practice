from encryption.encode_decode import Encryption

expressions = [("salam","AS^S_"),
               ("sfq","ATC"),
               ("ZcG","hQu")]

class Test:
    def __init__(self):
        self.key = 50

    def valid(self,exp):
        secret = ''
        for ch in exp:
            secret += chr(ord(ch) ^ self.key)
        return secret


test = Test()
for exp in expressions:
    assert test.valid(exp[0]) == exp[1],f"{exp[0]} should be {exp[1]}"