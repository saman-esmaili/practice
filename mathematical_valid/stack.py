class Stack():
    def __init__(self):
        self.stack = []
        self.top_index = -1

    def push(self, item):
        self.stack.append(item)
        self.top_index += 1

    def remove(self):
        self.stack.pop()
        self.top_index -= 1

    def is_empty(self):
        if self.top_index == -1:
            return True
        return False

    def has_item(self):
        if self.top_index >=0:
            return True
        return False
