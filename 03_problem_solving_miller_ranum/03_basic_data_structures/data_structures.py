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
        return self.items.pop()

    def remove_rear(self) -> Any:
        return self.items.pop(0)        

    def size(self) -> int:
        return len(self.items)

    def __repr__(self):
        return "Deque(" + str(self.items) + ")"        


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: 'Node' = None

    def get_data(self) -> Any:
        return self.data

    def get_next(self) -> 'Node':
        return self.next

    def set_data(self, data: Any) -> None:
        self.data = data

    def set_next(self, next: 'Node') -> None:
        self.next = next

    def __repr__(self):
        return "Node(" + str(self.data) + ")"  


class UnorderedList:
    def __init__(self) -> None:
        self.head: Node = None

    def is_empty(self) -> bool:
        return self.head == None

    def add(self, item: Any) -> None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self) -> int:
        count = 0
        current_node = self.head

        while current_node != None:
            count += 1
            current_node = current_node.get_next()

        return count

    def search(self, item: Any) -> bool:
        current_node = self.head
        found = False

        while not found and current_node != None:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()

        return found

    def remove(self, item: Any) -> None:
        current_node = self.head
        previous_node = None
        found = False

        while not found:
            if current_node.get_data() == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if previous_node == None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())


class OrderedList(UnorderedList):

    def __init__(self) -> None:
        self.head: Node = None

    def is_empty(self) -> bool:
        return self.head == None

    def add(self, item: Any) -> None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self) -> int:
        count = 0
        current_node = self.head

        while current_node != None:
            count += 1
            current_node = current_node.get_next()

        return count

    def search(self, item: Any) -> bool:
        # Assumes the list is in increasing order, starting with head
        current_node = self.head
        found = False
        stop = False

        while current_node != None and not found and not stop:
            if current_node.get_data() == item:
                found = True
            else:
                if current_node.get_data() > item:
                    stop = True
                else:
                    current_node = current_node.get_next()

        return found

    def add(self, item: Any) -> None:
        current_node = self.head
        previous_node = None
        stop = False

        while current_node != None and not stop:
            if current_node.get_data() > item:
                stop = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        temp = Node(item)
        if previous_node == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current_node)
            previous_node.set_next(temp)


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

    # d = Deque()
    # print(d.add_rear(4))
    # print(d.add_rear('dog'))
    # print(d.add_front('cat'))
    # print(d.add_front(True))    
    # print(d.size())
    # print(d.is_empty())    
    # print(d.add_rear(8.4))
    # print(d.remove_rear())
    # print(d.remove_front())    

    ul = UnorderedList()
    print(ul.add(31))
    print(ul.add(77))
    print(ul.add(17))
    print(ul.add(93))    
    print(ul.add(26))
    print(ul.add(54))

    print(ul.length())
    print(ul.search(17))    