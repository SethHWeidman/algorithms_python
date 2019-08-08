from data_structures import Stack

def symbol_checker(symbols: str) -> bool:
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbols) and balanced:
        symbol = symbols[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                left = s.pop()
                balanced = symbol_match(symbol, left)

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
    
def symbol_match(right: str, left: str) -> bool:
    starts = '({['
    ends = ')}]'
    return starts.index(left) == ends.index(right)
      

if __name__ == '__main__':
    test1 = '([])'
    test2 = '([)]'
    print(symbol_checker(test1))
    print(symbol_checker(test2))