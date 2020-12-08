N = int(input())
stack = []
result = ''
flag = True
check = [0 for _ in range(N+1)]
for _ in range(N):
    num = int(input())
    if len(stack) == 0 or stack[-1] < num:
        for n in range(1, num+1):
            if check[n] == 0:
                stack.append(n)
                result += '+'
                check[n] = 1
        stack.pop()
        result += '-'
    elif stack[-1] == num:
        stack.pop()
        result += '-'
    else:
        flag = False

if flag:
    for i in result:
        print(i)
else:
    print('NO')
