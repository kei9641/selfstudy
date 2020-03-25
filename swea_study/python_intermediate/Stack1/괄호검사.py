import sys
sys.stdin = open('괄호검사.txt')

T = int(input())
for tc in range(T):
    code = input()
    stack = []
    result = 1
    for s in code:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')':
            if len(stack) != 0:
                if stack[-1] != '(':
                    result = 0
                    break
                else:
                    stack.pop()
            else:
                result = 0
                break
        elif s == '}':
            if len(stack) != 0:
                if stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
            else:
                result = 0
                break
    if len(stack) != 0:
        result = 0
    print('#{} {}'.format(tc+1, result))