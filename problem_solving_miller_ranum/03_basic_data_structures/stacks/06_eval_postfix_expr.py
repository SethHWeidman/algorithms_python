import sys
sys.path.append('..') # allow import of code from one directory level up

from string import digits          
from data_structures import Stack

def eval_postfix_expr(postfix_expr: str) -> int:

    op_stack = Stack()

    tokens = postfix_expr.split()

    for token in tokens:
        # if a number, just push it onto the stack
        if token in digits:
            op_stack.push(int(token))
        # otherwise:
        # 1. pop the top two operands
        # 2. do the math with the token
        # 3. push the result back on
        else:
            operand2 = op_stack.pop()
            operand1 = op_stack.pop()
            res = do_math(token, operand1, operand2)
            op_stack.push(res)

    return op_stack.pop()

def do_math(token: str, operand1: int, operand2: int) -> int:
    if token == '+':
        return operand1 + operand2
    if token == '-':
        return operand1 - operand2
    if token == '*':
        return operand1 * operand2
    if token == '/':
        return operand1 / operand2                        


if __name__ == '__main__':
    s1 = '4 5 6 * +'
    s2 = '7 8 + 3 2 + /'
    print(eval_postfix_expr(s1))
    print(eval_postfix_expr(s2))