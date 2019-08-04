from __future__ import annotations
import os
from typing import Any

'''
Note: run 

export PYTHONHASHSEED=0

before running to get deterministic results
'''


class Node(object):

    def __init__(self, data: Any=None, next_node: Node=None) -> None:
        self.data = data
        self.next_node = next_node

    def get_data(self) -> Any:
        return self.data

    def get_next(self) -> Node:
        return self.next_node

    def set_next(self, new_next: Node) -> None:
        self.next_node = new_next

    def __repr__(self) -> str:
        return "Node(" + str(self.data) + ")"


class LinkedList(object):
    def __init__(self, head: Node=None):
        self.head = head

    def insert(self, data: Any=None) -> None:
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
        '''
        Assumes keys are strings
        '''
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
        

if __name__=="__main__":
    pass
    