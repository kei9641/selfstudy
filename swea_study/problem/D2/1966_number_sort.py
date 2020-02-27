T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('#{}'.format(tc+1), end=' ')
    print(*numbers)