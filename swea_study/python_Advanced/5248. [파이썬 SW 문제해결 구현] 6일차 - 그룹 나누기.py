from collections import deque
import sys
sys.stdin = open('5248. [파이썬 SW 문제해결 구현] 6일차 - 그룹 나누기.txt')

T = int(input())
for tc in range(1, T+1):
    q = deque()
    N, M = map(int, input().split())
    students = [0 for _ in range(N+1)]
    teams = [[] for _ in range(N+1)]
    papers = list(map(int, input().split()))
    group = 0

    for i in range(0, len(papers), 2):
        A = papers[i]
        B = papers[i+1]
        teams[A].append(B)
        teams[B].append(A)

    for i in range(1, N+1):
        if students[i] == 0:
            group += 1
            q.append(i)
            students[i] = 1
            while q:
                j = q.popleft()
                for team in teams[j]:
                    if students[team] == 0:
                        q.append(team)
                        students[team] = 1

    print('#{} {}'.format(tc, group))
