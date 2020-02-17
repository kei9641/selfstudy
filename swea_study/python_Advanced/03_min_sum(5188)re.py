import sys
sys.stdin = open('min_sum.txt')

# def isWall(x, y):
#     global N
#     if 0 <= x < N and 0 <= y < N:
#         return False
#     return True

minSum = 0

def route(x, y):
    global minSum, N
    dx = [1, 0]
    dy = [0, 1]
    minSum += board[x][y]
    if x == N-1 and y == N-1:
        sums.append(minSum)
        minSum = 0
    for n in range(2):
        if x+dx[n] >= N or y+dy[n] >= N:
            return
        route(x+dx[n], y+dy[n])
   
T = int(input())
for tc in range(T):
    N = int(input())
    board = []
    sums = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    route(0, 0)
    print(min(sums))
    

