from collections import deque
import sys
sys.stdin = open('5247. [파이썬 SW 문제해결 구현] 6일차 - 연산.txt')

def cal():
    global cnt
    while q:
        cnt, num = q.popleft()
        if num == M:
            return
        cnt += 1
        num1 = num + 1
        if 0 < num1 <= 1000000 and visit[num1] == 0:
            q.append((cnt, num1))
            visit[num1] = 1
        num2 = num - 1
        if 0 < num2 <= 1000000 and visit[num2] == 0:
            q.append((cnt, num2))
            visit[num2] = 1
        num3 = num * 2
        if 0 < num3 <= 1000000 and visit[num3] == 0:
            q.append((cnt, num3))
            visit[num3] = 1
        num4 = num - 10
        if 0 < num4 <= 1000000 and visit[num4] == 0:
            q.append((cnt, num4))
            visit[num4] = 1

T = int(input())
for tc in range(1, T+1):
    q = deque()
    visit = [0 for _ in range(1000001)]
    N, M = map(int, input().split())
    q.append((0, N))
    visit[N] = 1
    cnt = 0
    cal()
    print('#{} {}'.format(tc, cnt))