T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    sequence = [0] * N
    result = 0

    for i in range(N):
        sequence[i] = 1
        for j in range(i):
            if A[j] < A[i] and sequence[i] < sequence[j] + 1:
                sequence[i] = sequence[j] + 1
        if sequence[i] > result:
            result = sequence[i]
    print('#{} {}'.format(tc, result))
