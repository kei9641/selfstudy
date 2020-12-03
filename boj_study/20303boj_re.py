def totalCandy(x, y, n):
    if y > N:
        return
    if info[x][y] == 1:
        candy[n] += candy[y]
        candy[y] = 0
        info[x][y], info[y][x] = 0, 0
        friends[n] += friends[y]
        friends[y] = 0
        totalCandy(y, 1, n)
    totalCandy(x, y+1, n)

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
info = [[0 for _ in range(N+1)] for _ in range(N+1)]
friends = [1 for _ in range(N+1)]
steal = [0 for _ in range(K)]
for _ in range(M):
    a, b = map(int, input().split())
    info[a][b] = 1
    info[b][a] = 1

for x in range(1, N+1):
    for y in range(x+1, N+1):
        if info[x][y] == 1:
            totalCandy(x, y, x)

for i in range(N+1):
    for j in range(K-1, 0, -1):
        if friends[i] <= j:
            steal[j] = max(steal[j], steal[j-friends[i]]+candy[i])
print(steal[-1])