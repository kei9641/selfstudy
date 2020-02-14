T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    fly = []
    max_kill = 0
    for _ in range(N):
        fly.append(list(map(int,input().split()))) 
    startx = 0
    endx = M
    starty = 0
    endy = M
    for _ in range((N-M+1)**2):
        kill = 0
        for x in range(startx, endx):
            for y in range(starty, endy):
                kill += fly[x][y]
        if max_kill < kill:
            max_kill = kill
        starty += 1
        endy += 1
        if starty == N - M + 1:
            starty = 0
            endy = M
            startx += 1
            endx += 1
    print('#{} {}'.format(tc+1,max_kill))