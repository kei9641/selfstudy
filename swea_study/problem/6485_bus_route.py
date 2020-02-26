T = int(input())
for tc in range(T):
    N = int(input())
    A = []
    B = []
    result = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    for _ in range(P):
        count = 0
        C = int(input())
        for i in range(N):
            if A[i] <= C <= B[i]:
                count += 1
        result.append(count)
    print('#{}'.format(tc+1),end=' ')
    print(*result)
    