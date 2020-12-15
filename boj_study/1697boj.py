from collections import deque

N, K = map(int, input().split())
pos = [0 for _ in range(100001)]

seconds = deque()
seconds.append(N)

while seconds:
    x = seconds.popleft()

    if x == K:
        break

    for move in [x-1, x+1, 2*x]:
        if 0 <= move < 100001 and pos[move] == 0:
            seconds.append(move)
            pos[move] = pos[x] + 1

print(pos[K])
