from graph.graphs import Generator


class Relation():
    def __init__(self,node1,node2):
        self.node1 = node1
        self.node2 = node2
        generator = Generator()
        self.lables = generator.generate()[1]
        self.matrix = generator.generate()[0]
    def find_way(self):
        list = []
        for key,val in self.lables.items():
            if val == self.node1:
                list.append([key,0])
            elif val == self.node2:
                list.append([0,key])
            if len(list) == 2:
                break
        row = list[0][0] + list[1][0]
        col = list[0][1] + list[1][1]
        if self.matrix[row,col] == 1:
            return True
        else:
            return False


node1 = input("please enter first node:")
node2 = input("please enter second node:")

path = Relation(node1,node2)
print(path.find_way())