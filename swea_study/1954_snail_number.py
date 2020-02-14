T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] # 우하좌상
   

    def isWall(x, y):
        if 0 <= x < N and 0 <= y < N: # 벽을 만나면 True
            return False
        return True

    def isFull(x, y): # 값이 있는 곳을 만나면 True
        if arr[x][y] != 0:
            return True
        return False

    number = 1
    i = 0
    x, y = 0, 0

    while number < N ** 2:
        while (isWall(x+dx[i], y+dy[i]) == False) and (isFull(x+dx[i], y+dy[i]) == False):
            arr[x][y] = number
            number += 1
            x += dx[i]
            y += dy[i]
        i += 1
        if i == 4:
            i = 0
    arr[x][y] = number

    print('#{}'.format(tc+1))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()