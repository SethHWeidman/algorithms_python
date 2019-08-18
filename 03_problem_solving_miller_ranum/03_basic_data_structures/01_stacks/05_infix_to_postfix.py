import sys
sys.path.append('..') # allow import of code from one directory level up

from string import ascii_uppercase          
from data_structures import Stack

def infix_to_postfix(infix_expr: str) -> str:
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    op_stack = Stack()

    postfix_list = []

    token_list = infix_expr.split()

    for token in token_list:
        # if it is a letter, just add to list
        if token in ascii_uppercase:
            postfix_list.append(token)
        # if it is a left paren, push it on the op_stack            
        elif token == '(':
            op_stack.push(token)
        # if right paren            
        elif token == ')':
            # append first token in op stack to postfix_list
            # THEN keep going until you see a left paren
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()

        # otherwise, keep appending until you get to an operator of lower precedence
        else:
            while (not op_stack.isEmpty()) and \
                (prec[op_stack.peek()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
            
            op_stack.push(token)

    # handle the case where there are operators left on the stack at the end
    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())

    return ' '.join(postfix_list)

if __name__ == '__main__':
    s1 = '( A + B ) * ( C + D )'
    s2 = '( A + B ) * C'
    s3 = 'A + B * C'
    s4 = 'A * B * C * D * E'        
    s5 = 'A + B * C * D * E'   
    print(infix_to_postfix(s1))
    print(infix_to_postfix(s2))
    print(infix_to_postfix(s3))
    print(infix_to_postfix(s4))
    print(infix_to_postfix(s5))