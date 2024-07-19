import random


class Hash:
    def __init__(self):
        self.values = []
        self.keys = []
        self.size = 100
        self.index = 0

    def get_hash(self, key):
        if self.index <= self.size:
            if key not in self.keys:
                self.keys.append(key)
                self.address = self.index
                self.index += 1
                return self.address
        else:
            raise Exception("list is full")

    def set(self, val):
        if self.index <= self.size:
            self.values.insert(self.address, val)
        else:
            raise Exception("list is full")

    def get(self, key):
        for keys in self.keys:
            if key == keys:
                address = self.keys.index(key)
                return self.values[address]


hash = Hash()
for i in range(100):
    hash.get_hash(i)
    hash.set(random.randint(1, 50))
print(hash.get(54))
