class Queue:
    def __init__(self):
        self.queue = []
        self.top_index = -1

    def add(self,item):
        self.queue.append(item)
        self.top_index += 1

    def remove(self):
        if self.top_index >= 0:
            value = self.queue.pop(0)
            self.top_index -= 1
            return value
        raise Exception("queue is empty")


q = Queue()
q.add("a")
q.add("b")
q.add("c")
q.add("d")
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())