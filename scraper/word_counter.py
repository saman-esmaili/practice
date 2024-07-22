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
            split_list = self.list[i].split()
            length = len(split_list)
            for i2 in range(length):
                if self.word in split_list[i2]:
                    counter += 1
        return counter


word = input("enter a word:")
counter = Counter(word)
counter.read()
print(counter.count())
