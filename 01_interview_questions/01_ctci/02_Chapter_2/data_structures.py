from typing import Any

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
    '''
    Unordered list (items are not orderded)
    Every element added:
        (self.head = old_head)
        Old head becomes "next" of new element. (new.next = old_head))
        Becomes head (new == self.head)
    
    In some sense 
    '''
    def __init__(self) -> None:
        self.head: Node = None

    def is_empty(self) -> bool:
        return self.head == None

    def add(self, item: Any) -> None:
        temp = Node(item)
        old_head = self.head
        temp.set_next(old_head)
        self.head = temp

    def add_to_tail(self, item: Any) -> None:
        temp = Node(item)
        temp_last = self.head()
        while temp_last.get_next():
            temp_last = temp_last.get_next()
        temp_last.set_next(temp)

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
