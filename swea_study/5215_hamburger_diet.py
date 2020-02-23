def powerSet(n, m, Sum):
    if Sum > L:
        return
    if n == m:
        makeSet(n, Sum)
    else:
        A[m] = 1
        powerSet(n, m+1, Sum+K[m])
        A[m] = 0
        powerSet(n, m+1, Sum)
def makeSet(n, Sum):
    global taste, result
    for i in range(N):
        if A[i] == 1:
            taste += T[i]
    if result < taste:
        result = taste
    taste = 0
T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    T = []
    K = []
    taste = 0
    result = 0
    A = [0 for _ in range(N)]
    for _ in range(N):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    powerSet(N, 0, 0)
    print('#{} {}'.format(tc+1, result))
