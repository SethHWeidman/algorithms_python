import sys
sys.path.append('..') # allow import of code from one directory level up

from data_structures import Stack

def remainder_base_2(decimal_number: int) -> str:
    remainder_stack = Stack()

    while decimal_number > 0:
        remainder = decimal_number % 2
        remainder_stack.push(remainder)
        decimal_number = decimal_number // 2

    list_of_items = []
    while not remainder_stack.isEmpty():
        list_of_items.append(str(remainder_stack.pop()))

    return ''.join(list_of_items)

if __name__ == '__main__':
    test_num = 233
    print(remainder_base_2(233))