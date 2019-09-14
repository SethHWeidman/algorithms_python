from typing import Any


class HashTable(object):
    def __init__(self, size: int = 11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, 
                      key: int) -> int:
        return key % self.size

    def rehash(self, 
               old_hash: int) -> int:
        return (old_hash + 1) % self.size

    def put(self, 
            key: int, 
            data: Any) -> None:
        hash_value = self.hash_function(key)

        if not self.slots[hash_value]:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data

            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if not self.slots[next_slot]:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key: int) -> Any:
        '''
        Returns None if key not in Hash table
        '''
        start_slot = self.hash_function(key)

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] and not found and not stop:
            # keep rehashing until we find the element
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True 
                # we have gone through the entire hash table at this point
        return data

    def __getitem__(self, key: int) -> Any:
        return self.get(key)

    def __setitem__(self, key: int, data: Any) -> None:
        self.put(key, data)

if __name__=="__main__":
    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'

    print(h.slots)

    print(h.data)

    print(h[20])

    print(h[17])

    h[20] = 'duck'
    print(h[20])

    print(h.data)
    print(h[99])