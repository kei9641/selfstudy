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
    short = 10000
    turn = 0
    fastWay = 0
    while turn < 100:
        count = 0
        goalX = 0
        goalY = 0
        for idx in range(100): # 출발점 찾기
            if ladder[goalX][idx] == 1:
                goalY = idx
                ladder[goalX][idx] = 0
                break

        dx = [0, 0, 1] # 좌우하
        dy = [-1, 1, 0]

        while goalX != 99: # 도착점까지
            for i in range(0, 3):
                if isWall(goalX + dx[i], goalY + dy[i]) == False:
                    if ladder[goalX + dx[i]][goalY + dy[i]] == 1: # 1이 있는 쪽으로 이동
                        goalX += dx[i]
                        goalY += dy[i]
                        count += 1
                        if dx[i] == 0 and dy[i] == -1: # 좌측이면
                            dx = [1, 0, 0] # 하좌우
                            dy = [0, -1, 1]
                        elif dx[i] == 0 and dy[i] == 1: # 우측이면
                            dx = [1, 0, 0] # 하우좌
                            dy = [0, 1, -1] 
                        else: # 아래쪽이면
                            dx = [0, 0, 1] # 좌우하
                            dy = [-1, 1, 0]
                        break
        
        if count < short:
            short = count
            fastWay = idx

        if idx == 99:
            break
        turn += 1
    print('#{} {}'.format(tc+1, fastWay))