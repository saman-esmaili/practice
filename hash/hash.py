import random


class Hash:
    def __init__(self):
        self.values = []
        self.collisions = []
        self.size = 200
        self.index = 0

    def add_empty(self):
        for i in range(self.size):
            self.values.append("")

    def get_hash(self, key):
        if self.index <= self.size:
            result = ""
            if type(key) == int:
                self.address = key % 199
            elif type(key) == str:
                for ch in key:
                    result += str(ord(ch))
                reminder = str(int(result) % 100000007)
                self.address = reminder[-3:]
                if 0 <= int(self.address) <= 200:
                    self.address = int(self.address)
                else:
                    self.address = reminder[-2:]
                self.address = int(self.address)
            self.index += 1
            self.key = key
            return self.address
        raise Exception("list is full")

    def is_collision(self):
        if self.values[self.address] != "":
            return True
        return False

    def set(self, val):
        if self.index <= self.size:
            if self.is_collision():
                for i,place in enumerate(self.values):
                    if place == "":
                        self.values[i] = val
                        self.index_value = i
                        break
                self.collisions.append((self.key,self.index_value))
            else:
                self.values[self.address] = val

    def get(self, key):
        for item in self.collisions:
            if item[0] == key:
                address = item[1]
                return self.values[address]
        address = self.get_hash(key)
        self.index -= 1
        return self.values[address]


hash = Hash()
hash.add_empty()

hash.get_hash("saman")
hash.set("20")

hash.get_hash(31)
hash.set("collision_saman")

hash.get_hash("sport")
hash.set("football")

hash.get_hash("material")
hash.set("wooden")

hash.get_hash(69)
hash.set("collision_sport")

hash.get_hash(96)
hash.set("collision_material")

hash.get_hash("teacher")
hash.set("math")

print(hash.get("material"))
print(hash.get(31))
print(hash.get("teacher"))
print(hash.get("saman"))
print(hash.get(69))
print(hash.get(96))
print(hash.get("sport"))