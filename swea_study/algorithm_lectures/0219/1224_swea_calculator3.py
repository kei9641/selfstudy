import sys
sys.stdin = open('calculator3.txt')

T = 10
for tc in range(T):
    N = int(input())
    equations = list(input())
    change = []
    operator = []
    for equation in equations:
        if equation == '(':
            operator.append(equation)
        elif equation == '+':
            if operator[-1] == '(':
                operator.append(equation)
            else:
                change.append(operator.pop())
                operator.append(equation)
        elif equation == '*':
            if operator[-1] == '*':
                change.append(equation)
            else:
                operator.append(equation)
        elif equation == ')':
            while operator[-1] != '(':
                change.append(operator.pop())
            operator.pop()
        else:
            change.append(equation)
    stack = []
    for c in change:
        if c == '*':
            stack.append(stack.pop(-2) * stack.pop(-1))
        elif c == '+':
            stack.append(stack.pop(-2) + stack.pop(-1))
        else:
            stack.append(int(c))
    print('#{} {}'.format(tc+1, stack[0]))