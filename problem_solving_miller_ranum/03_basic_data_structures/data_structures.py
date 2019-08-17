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

    q = Queue()
    print(q.isEmpty())
    print(q.enqueue('dog'))
    print(q.enqueue(4))
    print(q.dequeue())    
    q = Queue()
    print(q.isEmpty())