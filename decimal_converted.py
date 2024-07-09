class Binary():
    def __init__(self,number,base):
        self.number = number
        self.base = base

    def convert_binary(self):
        self.binaries = ''
        while self.number > 0:
            reminder = self.number % self.base
            self.number = self.number // self.base
            self.binaries += str(reminder)
        return self.binaries[::-1]


binary = Binary(113,2)
print(binary.convert_binary())

