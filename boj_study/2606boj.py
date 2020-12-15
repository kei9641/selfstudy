from collections import deque

n = int(input())
m = int(input())
connect = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

result = 0
deq = deque([1])
visit = [0 for _ in range(n+1)]
visit[1] = 1
while deq:
    computer = deq.popleft()
    for com in connect[computer]:
        if visit[com] == 0:
            visit[com] = 1
            deq.append(com)
            result += 1

print(result)