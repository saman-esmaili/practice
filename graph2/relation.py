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
        past_row = row
        result = ""
        if self.matrix[row,col] == 1:
            return True
        else:
            while result != self.node2:
                length = len(self.list.queue)
                for key in self.labels:
                    col = self.labels[key]
                    if self.matrix[row,col] == 1:
                        if key not in self.list.queue:
                            self.list.add(key)
                            row = col
                            result = key
                            break
                if col == len(self.labels)-1:
                    if row == past_row:
                        return False

                if len(self.list.queue) <= length:
                    row = self.labels[self.node1]

            return True


node1 = input("please enter first node:")
node2 = input("please enter second node:")

# node1 = "C"
# node2 = "F"
graph = Relation(node1, node2)
print(graph.relation())
