T = int(input())
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    result = max(num)
    for s in range(0, N):
        for e in range(s+2, N+1):
            if sum(num[s:e]) > result:
                result = sum(num[s:e])

    print('#{} {}'.format(tc+1, result))