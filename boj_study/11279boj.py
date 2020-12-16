import sys
import heapq

a = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(a, -x)
    elif a:
        print(-heapq.heappop(a))
    else:
        print(0)

