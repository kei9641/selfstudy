T = int(input())
for tc in range(1, T+1):
    W, H, N = map(int, input().split())
    x = []
    y = []
    move = 0
    for _ in range(N):
        x0, y0= map(int, input().split())
        x.append(x0)
        y.append(y0)
    for i in range(N-1):
        if (x[i]<x[i+1] and y[i]<y[i+1]) or (x[i]>x[i+1] and y[i]>y[i+1]):
            move += max(abs(x[i]-x[i+1]), abs(y[i]-y[i+1]))
        else:
            move += abs(x[i]-x[i+1]) + abs(y[i]-y[i+1])
    print('#{} {}'.format(tc, move))
