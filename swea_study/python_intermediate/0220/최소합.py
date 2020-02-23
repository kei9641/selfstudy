import sys
sys.stdin = open('최소합.txt')

def dfs(x):
    global Sum, result
    if Sum > result:
        return
    if x == N:
        if Sum < result:
            result = Sum
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            Sum += arr[x][i]
            dfs(x+1)
            visited[i] = 0
            Sum -= arr[x][i]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0 for _ in range(N)]
    Sum = 0
    result = 987654321
    dfs(0)
    print('#{} {}'.format(tc+1, result))