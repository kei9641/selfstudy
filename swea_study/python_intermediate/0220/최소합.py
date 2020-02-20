import sys
sys.stdin = open('최소합.txt')

summ = 0

def dfs(x):
    global result, summ
    if x == N:
        if result > summ:
            result = summ
        return
    for y in range(N):
        if visited[y] == 0:
            if summ + arr[x][y] 
            summ += arr[x][y]
            visited[y] = 1
            dfs(x+1)
            visited[y] = 0
            summ -= arr[x][y]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    result = 987654321
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0 for _ in range(N)]
    dfs(0)
    print('#{} {}'.format(tc+1, result))