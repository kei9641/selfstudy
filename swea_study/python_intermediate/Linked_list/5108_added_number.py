T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(M):
        i, n = map(int, input().split())
        if i <= L:
            numbers.insert(i, n)
    print('#{} {}'.format(tc, numbers[L]))