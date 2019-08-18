from typing import Any

class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def peek(self) -> Any:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def __repr__(self):
        return "Stack(" + str(self.items) + ")"


class Queue:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def enqueue(self, item: Any) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> Any:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def __repr__(self):
        return "Queue(" + str(self.items) + ")"


class Deque:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def add_front(self, item: Any) -> None:
        self.items.append(item)

    def add_rear(self, item: Any) -> None:
        self.items.insert(0, item)

    def remove_front(self) -> Any:
        self.items.pop()

    def remove_rear(self) -> Any:
        self.items.pop(0)        

    def size(self) -> int:
        return len(self.items)

    def __repr__(self):
        return "Deque(" + str(self.items) + ")"        


if __name__ == '__main__':
    # s = Stack()
    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.isEmpty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())

    # q = Queue()
    # print(q.isEmpty())
    # print(q.enqueue('dog'))
    # print(q.enqueue(4))
    # print(q.dequeue())    
    # q = Queue()
    # print(q.isEmpty())

    d = Deque()
    print(d.add_rear(4))
    print(d.add_rear('dog'))
    print(d.add_front('cat'))
    print(d.add_front(True))    
    print(d.size())
    print(d.is_empty())    
    print(d.add_rear(8.4))
    print(d.remove_rear())
    print(d.remove_front())    