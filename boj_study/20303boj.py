import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
candy = list(map(int, sys.stdin.readline().split()))
visit = [0 for _ in range(N)]
connect = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connect[a].append(b)
    connect[b].append(a)

bag = []
search = deque()
for n in range(1, N+1):
    if visit[n-1] == 0:
        children = 0
        amount = 0
        search.append(n)
        visit[n-1] = 1
        
    while search:
        node = search.popleft()
        children += 1
        amount += candy[node-1]
        for link in connect[node]:
            if visit[link-1] == 0:
                search.append(link)
                visit[link-1] = 1

    bag.append((children, amount))
    children = 0
    amount = 0

steal = [0 for _ in range(K)]
for i in range(len(bag)):
    for j in range(K-1, -1, -1):
        if bag[i][0] <= j:
            steal[j] = max(steal[j], steal[j-bag[i][0]]+bag[i][1])

print(steal[-1])