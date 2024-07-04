class Binary():
    def __init__(self,number,base):
        self.number = number
        self.base = base

    def convert_binary(self):
        self.binaries = []
        while self.number // self.base != 0:
            result = self.number % self.base
            self.binaries.append(result)
            self.number = self.number // self.base
        self.binaries.append(self.number)
        return self.binaries[::-1]


binary = Binary(160,2)
print(binary.convert_binary())

