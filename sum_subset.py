class SumSubset():
    def __init__(self):
        self.number = int(input("Enter number:"))
        self.summation()
    def summation(self):
        lists = []
        total = 0
        for i in range(1,self.number):
            for i2 in range(1,self.number):
                for i3 in range(1,self.number):
                    total = i + i2 +i3
                    if total == self.number:
                        mylist = sorted([i,i2,i3])
                        if mylist not in lists:
                            lists.append(mylist)

        print(lists)

SumSubset()