# 좌표간 거리를 2차원 배열에 저장해서 시간줄이기(memoization)

def dfs(x, y, d):
    global result
    if result < d:
        return
    if visited.count(1) == N:
        d += abs(x-pos[2]) + abs(y-pos[3])
        if result > d:
            result = d
        return
    for i in range(4, 2*N+4, 2):
        if visited[(i-4)//2] == 0:
            visited[(i-4)//2] = 1
            dfs(pos[i], pos[i+1], d+(abs(x-pos[i])+abs(y-pos[i+1])))
            visited[(i-4)//2] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pos = list(map(int, input().split()))
    visited = [0 for _ in range(N)]
    result = 2000
    dfs(pos[0], pos[1], 0)
    print('#{} {}'.format(tc, result))