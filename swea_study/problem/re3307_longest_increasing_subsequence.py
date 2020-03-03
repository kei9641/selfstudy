def powerSet(n, k):
    global longesst
    if n == k:
        sub = []
        for i in range(N):
            if A[i] == 1:
                sub.append(sequence[i])
        num = 0
        for i in range(len(sub)):
            if sub[i] < num:
                return
            num = sub[i]
        if len(sub) > longesst:
            longesst = len(sub)
    else:
        A[k] = 1
        powerSet(n, k+1)
        A[k] = 0
        powerSet(n, k+1)

T = int(input())
for tc in range(T):
    N = int(input())
    sequence = list(map(int, input().split()))
    A = [0 for _ in range(N)]
    longesst = 0
    powerSet(N, 0)
    print('#{} {}'.format(tc+1, longesst))
    