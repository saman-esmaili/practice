import random


class Hash:
    def __init__(self):
        self.values = []
        self.size = 100
        self.index = 0

    def get_hash(self,key):
        if self.index <= self.size:
            self.address = self.index
            self.index += 1
            self.key = key
            return self.address
        raise Exception("list is full")

    def set(self,val):
        if self.index <= self.size:
            self.values.insert(self.address,val)
        else:
            raise Exception("list is full")

    def get(self,key):
        if key == self.key:
            value = self.values[self.address]
            return value

hash = Hash()
hash.get_hash("A")
hash.set(4)
print(hash.get("A"))
hash.get_hash("A")
hash.set(5)
print(hash.get("A"))