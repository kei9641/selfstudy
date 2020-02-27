T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sums = []
    multiple_sum = 0
    max_sum = 0

    if N <= M:
        for n in range(M-N+1):
            for i in range(N):
                multiple_sum += A[i] * B[i+n]
            sums.append(multiple_sum)
            multiple_sum = 0
    elif M < N:
        for n in range(N-M+1):
            for i in range(M):
                multiple_sum += A[i+n] * B[i]
            sums.append(multiple_sum)
            multiple_sum = 0
    for i in range(len(sums)):
        if max_sum < sums[i]:
            max_sum = sums[i]
    print('#{} {}'.format(tc+1, max_sum))