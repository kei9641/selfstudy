def square(n, k):
    global result
    if n == k:
        return
    result *= N
    square(n+1, k)

T = 10
for _ in range(T):
    tc = int(input())
    N, M = map(int, input().split())
    result = N
    square(1, M)
    print('#{} {}'.format(tc, result))