def find(x):
    global result
    if x == 0:
        result = 1
        return
    for y in range(100):
        if path[x][y] == 1:
            find(y)

T = 10
for _ in range(T):
    tc, N = map(int, input().split())
    M = list(map(int, input().split()))
    path = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(0, N*2, 2):
        path[M[i+1]][M[i]] = 1
    result = 0
    find(99)
    print('#{} {}'.format(tc, result))
