for tc in range(10):
    T = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    
    def isWall(x, y):
        result = True
        if 0 <= x < 100 and 0 <= y < 100:
            result = False
        return result

    goalX = 99
    goalY = 0
    for idx in range(100): # 도착점 찾기
        if ladder[goalX][idx] == 2:
            goalY = idx

    dx = [0, 0, -1] # 좌우상
    dy = [-1, 1, 0]

    while goalX != 0: # 출발점까지
        for i in range(0, 3):
            if isWall(goalX + dx[i], goalY + dy[i]) == False:
                if ladder[goalX + dx[i]][goalY + dy[i]] == 1: # 1이 있는 쪽으로 이동
                    goalX += dx[i]
                    goalY += dy[i]
                    if dx[i] == 0 and dy[i] == -1: # 좌측이면
                        dx = [-1, 0, 0] # 상좌우
                        dy = [0, -1, 1]
                    elif dx[i] == 0 and dy[i] == 1: # 우측이면
                        dx = [-1, 0, 0] # 상우좌
                        dy = [0, 1, -1] 
                    else: # 위쪽이면
                        dx = [0, 0, -1] # 좌우상
                        dy = [-1, 1, 0]
                    break
    print('#{} {}'.format(tc+1, goalY))