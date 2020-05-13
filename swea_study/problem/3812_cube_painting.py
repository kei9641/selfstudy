T = int(input())
for tc in range(1, T+1):
    X, Y, Z, A, B, C, N = map(int, input().split())
    color = [0 for _ in range(N)]
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                i = (abs(x-A)+abs(y-B)+abs(z-C)) % N
                color[i] += 1
    print('#{} '.format(tc), end='')
    print(*color)
