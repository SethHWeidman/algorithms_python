import os
from typing import Any, List

"""
Note: run 

export PYTHONHASHSEED=0

before running to get deterministic results
"""


class Node(object):
    def __init__(self, data: Any = None, next_node: "Node" = None) -> None:
        self.data = data
        self.next_node = next_node

    def get_data(self) -> Any:
        return self.data

    def get_next(self) -> "Node":
        return self.next_node

    def set_next(self, new_next: "Node") -> None:
        self.next_node = new_next

    def __repr__(self) -> str:
        return "Node(" + str(self.data) + ")"


class LinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def insert(self, data: Any = None) -> None:
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data: Any) -> Node:
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data: Any) -> None:
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __iter__(self) -> Node:
        current = self.head
        while current is not None:
            yield current
            current = current.get_next()

    def __repr__(self) -> str:
        return "[{}]".format(", ".join(map(str, self)))


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for i in range(size)]

    def hashing_function(self, key: str):
        """
        Assumes keys are strings
        """
        return hash(key) % self.size

    def insert(self, key: str) -> None:
        hash_bucket = self.hashing_function(key)
        list_entry = self.table[hash_bucket]
        list_entry.insert(key)

    def get(self, key: str) -> Node:
        hash_bucket = self.hashing_function(key)
        return self.table[hash_bucket].search(key)

    def __iter__(self) -> Node:
        for linked_list in self.table:
            yield linked_list

    def __repr__(self) -> Node:
        table_list = ["LinkedList(" + str(ll) + ")" for ll in self.table]
        return "[{}]".format(", ".join(map(str, table_list)))


class DynamicArray(object):
    """ 
    DYNAMIC ARRAY CLASS (Similar to Python List) 
    """

    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.arr = self.make_array(self.capacity)

    def __len__(self) -> int:
        """ 
        Return number of elements sorted in array 
        """
        return self.n

    def __getitem__(self, i: Any):
        """ 
        Return element at index i 
        """
        if not 0 <= i < self.n:
            # Check it k index is in bounds of array
            return IndexError("I is out of bounds !")

        return self.arr[i]  # Retrieve from the array at index k

    def append(self, ele: Any):
        """ 
        Add element to end of the array 
        """
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)

        self.arr[self.n] = ele  # Set self.n index to element
        self.n += 1

    def _resize(self, new_cap: int):
        """ 
        Resize internal array to capacity new_cap 
        """

        big = self.make_array(new_cap)  # New bigger array

        for i in range(self.n):  # Reference all existing values
            big[i] = self.arr[i]

        self.arr = big  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap: int):
        """ 
        Returns a new array with new_cap capacity 
        """
        return new_cap * [0]

    def __repr__(self) -> str:
        return str(self.arr)


class StringBuilder(object):
    """ 
    StringBuilder class that creates a single long string from a list of strings.
    """

    def __init__(self):
        self.arr = DynamicArray()

    def build_string(self, in_list: List[str]):
        for s in in_list:

            self.arr.append(s)

        return " ".join(self.arr.arr)  # TODO: use "getter" heres


if __name__ == "__main__":
    L = ["This", "is", "a", "sentence."]
    print(StringBuilder().build_string(L))
