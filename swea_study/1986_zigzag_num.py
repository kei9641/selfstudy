T = int(input())
for tc in range(T):
    N = int(input())
    result = 0
    for num in range(1, N+1):
        if num % 2 == 0:
            result -= num
        else:
            result += num
    print('#{} {}'.format(tc+1, result))