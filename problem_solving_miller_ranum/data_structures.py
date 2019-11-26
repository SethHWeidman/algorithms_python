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
        self.next: "Node" = None

    def get_data(self) -> Any:
        return self.data

    def get_next(self) -> "Node":
        return self.next

    def set_data(self, data: Any) -> None:
        self.data = data

    def set_next(self, next: "Node") -> None:
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
        UnorderedList.__init__(self)

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


class BinaryTree(object):
    def __init__(self, val: int):
        self.key = val
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, val: int) -> None:
        """
        Note: accepts an integer as a value (not a tree), and inserts value as the left child of the root.
        """
        if not self.left_child:
            self.left_child = BinaryTree(val)
        else:
            new_tree = BinaryTree(val)
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right_child(self, val: int) -> None:
        """
        Note: accepts an integer as a value (not a tree), and inserts value as the right child of the root.
        """
        if not self.right_child:
            self.right_child = BinaryTree(val)
        else:
            new_tree = BinaryTree(val)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def get_left_child(self) -> "BinaryTree":
        return self.left_child

    def get_right_child(self) -> "BinaryTree":
        return self.right_child

    def set_root_val(self, val: int) -> None:
        self.key = val

    def get_root_val(self) -> int:
        return self.key
