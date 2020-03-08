T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    bag = [[0 for _ in range(K+1)] for _ in range(N)]
    V = []
    C = []
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)
    for j in range(1, K+1):
        if j >= V[0]:
            bag[0][j] = C[0]
    for i in range(1, N):
        for j in range(1, K+1):
            if j >= V[i]:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j-V[i]]+C[i])
            else:
                bag[i][j] = bag[i-1][j]

    print('#{} {}'.format(tc, bag[N-1][K]))

# DP의 정석
# 부분집합을 사용하면 2^N
# 이 방식을 사용하면 N*(K+1)