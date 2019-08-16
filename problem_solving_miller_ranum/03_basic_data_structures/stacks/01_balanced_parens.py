import sys
sys.path.append('..') # allow import of code from one directory level up

from data_structures import Stack

def paren_checker(symbols: str) -> bool:
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbols) and balanced:
        symbol = symbols[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
       

if __name__ == '__main__':
    test1 = '(()()()())'
    test2 = '(((((((())'
    print(paren_checker(test1))
    print(paren_checker(test2))