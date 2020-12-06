N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(0, N):
    sumNum = 0
    n = 0
    while sumNum <= M:
        if sumNum == M:
            count += 1
            break
        if i+n == N:
            break
        sumNum += A[i+n]
        n += 1
print(count)