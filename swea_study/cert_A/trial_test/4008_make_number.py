def cal(a, idx):
    if idx+1 == N:
        result.append(a)
        return
    b = numbers[idx+1]
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                cal(a+b, idx+1)
            elif i == 1:
                cal(a-b, idx+1)
            elif i == 2:
                cal(a*b, idx+1)
            elif i == 3:
                cal(int(a/b), idx+1)
            operator[i] += 1
            
T = int(input())
for tc in range(T):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = []
    num1 = numbers[0]
    cal(num1, 0)
    print('#{} {}'.format(tc+1, max(result)-min(result)))
