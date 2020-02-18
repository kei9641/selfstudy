import sys
sys.stdin = open('min_sum.txt')

route = 0

def dfs(x, y):
    global route, result
    if x == N-1 and y == N-1:
        route += board[x][y]
        if result > route:
            result = route
    elif x == N-1:
        route += board[x][y]
        dfs(x, y+1)
    elif y == N-1:
        route += board[x][y]
        dfs(x+1, y) 
    else:
        route += board[x][y]
        dfs(x+1, y)
        dfs(x, y+1)
    route -= board[x][y]
   
T = int(input())
for tc in range(T):
    N = int(input())
    board = []
    
    result = 987654321
    for _ in range(N):
        board.append(list(map(int, input().split())))
    dfs(0, 0)
    print('#{} {}'.format(tc+1, result))

# sum 함수를 사용하면 시간이 더 걸림