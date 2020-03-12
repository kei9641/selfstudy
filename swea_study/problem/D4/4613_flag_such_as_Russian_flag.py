def check(n, k, p):
    global result
    if n == k:
        if result > p:
            result = p
        return
    if color != [] and color[-1] == 'B':
        check(n+1, k, p + (M - flag[n].count('B')))
        color.append('R')
        check(n+1, k, p + (M - flag[n].count('R')))
    elif color != [] and color[-1] == 'R':
        check(n+1, k, p + (M - flag[n].count('R')))
    else:
        if n == k-1:
            color.append('B')
            check(n+1, k, p + (M - flag[n].count('B')))
        else:
            check(n+1, k, p + (M - flag[n].count('W')))
            color.append('B')
            check(n+1, k, p + (M - flag[n].count('B')))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = []
    for _ in range(N):
        flag.append(input())
    paint = 0
    result = 10000
    for i in range(N):
        if i == 0:
            paint += M - flag[i].count('W')
        elif i == N-1:
            paint += M - flag[i].count('R')
    color = []
    check(1, N-1, paint)
    print('#{} {}'.format(tc, result))