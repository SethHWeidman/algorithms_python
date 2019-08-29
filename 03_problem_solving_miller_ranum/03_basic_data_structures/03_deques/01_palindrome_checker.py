import sys
sys.path.append('..') # allow import of code from one directory level up

from data_structures import Deque

def palindrome_checker(in_str: str) -> bool:
    d = Deque()
    
    for char in in_str:
        d.add_rear(char)

    still_equal = True

    while d.size() > 1 and still_equal:
        first = d.remove_front()
        last = d.remove_rear()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    print(palindrome_checker("abc"))
    print(palindrome_checker("aba"))