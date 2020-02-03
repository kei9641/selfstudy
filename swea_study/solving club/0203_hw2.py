T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    dx = [1, 0, -1, 0] # 우하좌상
    dy = [0, 1, 0, -1]

    def isWall(x, y):
        if 0 <= x < 5 and 0 <= y < 5: # 벽을 만나면 회전
            return False
        return True

    def isEmpty(x, y): # 값이 있는 곳을 만나면 회전
        if arr[x][y] != 0:
            return False
        return True

    number = 1
    i = 0
    x = 0
    y = 0

    while number < N ** 2:
        arr[y][x] = number
        number += 1
        while (isWall(x+dx[i], y+dy[i]) == False) and (isEmpty(x+dx[i], y+dy[i]) == False):
            x += dx[i]
            y += dy[i]
        i += 1
        print(arr)
    


