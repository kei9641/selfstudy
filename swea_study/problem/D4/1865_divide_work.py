def divide(n, k, p):
    global maxP
    if p <= maxP:
        return
    if n == k:
        if maxP < p:
            maxP = p
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            divide(n+1, k, p*(work[n][i]/100))
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    percent = 100
    maxP = 0
    divide(0, N, percent)
    print('#{0} {1:.6f}'.format(tc, maxP))
