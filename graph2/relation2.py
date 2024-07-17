from graph2.Q import Queue
from graph2.generate_graph import Graph


class Relation:
    def __init__(self, node1, node2):
        graph_generator = Graph()
        self.matrix = graph_generator.generate()[1]
        self.labels = graph_generator.generate()[0]
        self.node1 = node1
        self.node2 = node2

    def relation(self):
        self.list = Queue()
        row = self.labels[self.node1]
        col = self.labels[self.node2]
        self.list.add(self.node1)
        result = ""
        added = False
        first_turn = True
        if self.matrix[row,col] == 1:
            return True
        else:
            while result != self.node2:
                if row == self.list.queue[0] or not added:
                    if not first_turn:
                        start = self.labels[self.list.queue[1]]+1
                    else:
                        start = 0
                        first_turn = False
                else:
                    start = 0
                added = False
                for i,key in enumerate(self.labels,start=start):
                    col = i
                    if col == 7 and self.matrix[row,col] == 0:
                        break
                    if self.matrix[row,col] == 1:
                        key = list(self.labels.keys())[list(self.labels.values()).index(i)]
                        if key in self.list.queue:
                            return False
                        self.list.add(key)
                        result = key
                        row = col
                        added = True
                        break
                val = list(self.labels.values())[list(self.labels.keys()).index(self.list.queue[0])]
                if not added:
                    if row == val:
                        self.list.remove()
                    if self.list.has_item():
                        row = self.labels[self.list.queue[0]]
                    else:
                        return False

            return True


node1 = input("please enter first node:")
node2 = input("please enter second node:")
#
# node1 = "B"
# node2 = "H"
graph = Relation(node1, node2)
print(graph.relation())
