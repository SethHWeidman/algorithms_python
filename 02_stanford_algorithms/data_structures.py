class Queue:
    """
    FIFO Queue
    """

    def __init__(self, input_list=[]):
        self.list = input_list

    def push(self, el):
        self.list.append(el)

    def pop(self):
        a = self.list.pop(0)
        return a

    def is_empty(self):
        return len(self.list) == 0


class Stack:
    """
    LIFO Stack
    """

    def __init__(self, input_list=[]):
        self.list = input_list

    def push(self, el):
        self.list.append(el)

    def pop(self):
        a = self.list.pop()
        return a

    def is_empty(self):
        return len(self.list) == 0
