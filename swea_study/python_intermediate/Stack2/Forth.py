# import sys
# sys.stdin = open('Forth.txt')

T = int(input())
for tc in range(T):
    equation = list(input().split())
    operator = ['+', '-', '*', '/']
    stack = []
    result = ''

    for eq in equation:
        if eq == '.':
            if len(stack) == 1:
                result = str(stack.pop())
            else:
                result = 'error'
        elif eq in operator:
            if len(stack) >= 2:
                if eq == '+':
                    stack.append(stack.pop(-2) + stack.pop(-1))
                elif eq == '-':
                    stack.append(stack.pop(-2) - stack.pop(-1))  
                elif eq == '*':
                    stack.append(stack.pop(-2) * stack.pop(-1)) 
                elif eq == '/':
                    stack.append(stack.pop(-2) // stack.pop(-1)) 
            else:
                result = 'error'
                stack.append(0)
        else:
            stack.append(int(eq))

    print('#{} {}'.format(tc+1, result))