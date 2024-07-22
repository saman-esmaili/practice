import random


class Hash:
    def __init__(self):
        self.values = []
        self.size = 100
        self.index = 0

    def add_empty(self):
        for i in range(self.size - len(self.values)):
            self.values.append("")

    def get_hash(self, key):
        if self.index <= self.size:
            result = ""
            if type(key) == int:
                self.address = key % 97
            elif type(key) == str:
                for ch in key:
                    result += str(ord(ch))
                reminder = str(int(result) % 100000007)
                self.address = reminder[len(reminder) - 2:]
                self.address = int(self.address)
            self.index += 1
            return self.address
        raise Exception("list is full")

    def set(self, val):
        if self.index <= self.size:
            self.values[self.address] = val

    def get(self, key):
        self.address = self.get_hash(key)
        return self.values[self.address]


hash = Hash()
hash.add_empty()




