T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)]
    for i in range(1, Q+1):
        s, e = map(int, input().split())
        for j in range(s-1, e):
            box[j] = i
    print('#{}'.format(tc+1),end=' ')
    print(*box)
