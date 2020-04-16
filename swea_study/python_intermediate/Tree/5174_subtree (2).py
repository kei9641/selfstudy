import sys
sys.stdin = open('5174_subtree.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    line = list(map(int, input().split()))
    node = [[0]*3 for _ in range(E+2)]
    for i in range(0, 2*E, 2):
        if node[line[i]][0] == 0:
            node[line[i]][0] = line[i+1]
        else:
            node[line[i]][1] = line[i+1]
        node[line[i+1]][2] = line[i]
    result = 1
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        for idx in range(E+2):
            if node[idx][2] == x:
                q.append(idx)
                result += 1
    print('#{} {}'.format(tc, result))