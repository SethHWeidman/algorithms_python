import sys
sys.path.append('..') # allow import of code from one directory level up

from data_structures import Queue
from typing import List

def hot_potato(name_list: List[str], num: int) -> str:
    hot_potato_queue = Queue()
    for name in name_list:
        hot_potato_queue.enqueue(name)

    while hot_potato_queue.size() > 1:
        for _ in range(num):
            hot_potato_queue.enqueue(hot_potato_queue.dequeue())
        
        hot_potato_queue.dequeue()
        print(hot_potato_queue)

    return hot_potato_queue.dequeue()


if __name__ == '__main__':
    print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))