import sys
import heapq

N = int(sys.stdin.readline())
a = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if a:
            print(heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a, x)
