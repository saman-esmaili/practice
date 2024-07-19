class Counter():
    def __init__(self, word):
        self.list = []
        self.word = word

    def read(self):
        file = open("paragraphs.csv", "r")
        lines = file.readlines()
        for line in lines:
            self.list.append(line)

    def count(self):
        counter = 0
        for i in range(len(self.list)):
            for i2 in range(len(self.list[i].split())):
                if self.word == self.list[i].split()[i2]:
                    counter += 1
        return counter


word = input("enter a word:")
counter = Counter(word)
counter.read()
print(counter.count())
