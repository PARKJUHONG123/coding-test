import sys, collections

s = sys.stdin.readline().rstrip()
operators = ['-', '+', '*', '/']

def check_op(op):
    if op in ['(', ')']:
        return 0
    elif op in ['+', '-']:
        return 1
    else:
        return 2

def postfix():
    result = []
    stack = list()
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack:
                top = stack.pop()
                if top != '(':
                    result.append(top)
                else:
                    break
        elif c in operators:
            while stack:
                top = stack.pop()
                if check_op(c) <= check_op(top):
                    if top != '(':
                        result.append(top)
                    else:
                        stack.append(top)
                        break
                else:
                    stack.append(top)
                    break
            stack.append(c)
        else:
            result.append(c)

    while stack:
        result.append(stack.pop())
    return ''.join(result)

print(postfix())