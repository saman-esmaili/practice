class Queue():
    def __init__(self):
        self.queue = []
        self.top_index = -1
    def add(self,item):
        self.queue.append(item)
        self.top_index += 1

    def remove(self):
        self.queue.pop(0)
        self.top_index -= 1

    def has_item(self):
        if self.top_index >-1:
            return True
        else:
            return False



