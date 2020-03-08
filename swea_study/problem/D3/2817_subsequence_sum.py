def sumSub(n):
    global count
    result = 0
    for i in range(n):
        if sub[i] == 1:
            result += A[i]
        if result > K:
            return
    if result == K:
        count += 1

def makeSub(n, k):
    if n == k:
        sumSub(n)
    else:
        sub[n] = 1
        makeSub(n+1, k)
        sub[n] = 0
        makeSub(n+1, k)
    
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sub = [0 for _ in range(N)]
    count = 0
    makeSub(0, N)
    print('#{} {}'.format(tc, count))