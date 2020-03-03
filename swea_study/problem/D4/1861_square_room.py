dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def knock(x, y):
    global count
    count += 1
    for n in range(4):
        if isWall(x+dx[n], y+dy[n]) == False and room[x+dx[n]][y+dy[n]] == room[x][y]+1:
            knock(x+dx[n], y+dy[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))
    count = 0
    move = 0
    num = 0
    for x in range(N):
        for y in range(N):
            count = 0
            knock(x, y)
            if count > move:
                move = count
                num = room[x][y]
            elif count == move:
                if num > room[x][y]:
                    num = room[x][y]
    print('#{} {} {}'.format(tc, num, move))