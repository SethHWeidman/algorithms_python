from data_structures import Stack

def divide_by_base(decimal_number: int,
                   base: int) -> str:

    digits = "0123456789ABCDEF"

    remainder_stack = Stack()

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.push(digits[remainder])
        decimal_number = decimal_number // base

    list_of_items = []
    while not remainder_stack.isEmpty():
        list_of_items.append(str(remainder_stack.pop()))

    return ''.join(list_of_items)

if __name__ == '__main__':
    test_num = 233
    print(divide_by_base(233, 3))