T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    commends = list(input())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    direction = ['^', 'v', '<', '>']
    obstacle = ['*', '#', '-']
    for x0 in range(H):
        for y0 in range(W):
            if field[x0][y0] in direction:
                x, y = x0, y0
                break
    for commend in commends:
        if commend == 'S':
            way = direction.index(field[x][y])
            for n in range(20):
                if not (0 <= x+dx[way]*n < H and 0 <= y+dy[way]*n < W):
                    break
                if field[x+dx[way]*n][y+dy[way]*n] == '#':
                    break
                if field[x+dx[way]*n][y+dy[way]*n] == '*':
                    field[x+dx[way]*n][y+dy[way]*n] = '.'
                    break
        elif commend == 'U':
            if 0 <= x+dx[0] < H and 0 <= y+dy[0] < W and field[x+dx[0]][y+dy[0]] not in obstacle:
                field[x][y] = '.'
                field[x+dx[0]][y+dy[0]] = '^'
                x, y = x+dx[0], y+dy[0]
            else:
                field[x][y] = '^'
        elif commend == 'D':
            if 0 <= x+dx[1] < H and 0 <= y+dy[1] < W and field[x+dx[1]][y+dy[1]] not in obstacle:
                field[x][y] = '.'
                field[x+dx[1]][y+dy[1]] = 'v'
                x, y = x+dx[1], y+dy[1]
            else:
                field[x][y] = 'v'
        elif commend == 'L':
            if 0 <= x+dx[2] < H and 0 <= y+dy[2] < W and field[x+dx[2]][y+dy[2]] not in obstacle:
                field[x][y] = '.'
                field[x+dx[2]][y+dy[2]] = '<'
                x, y = x+dx[2], y+dy[2]
            else:
                field[x][y] = '<'
        elif commend == 'R':
            if 0 <= x+dx[3] < H and 0 <= y+dy[3] < W and field[x+dx[3]][y+dy[3]] not in obstacle:
                field[x][y] = '.'
                field[x+dx[3]][y+dy[3]] = '>'
                x, y = x+dx[3], y+dy[3]
            else:
                field[x][y] = '>'
    print('#{}'.format(tc), end=' ')
    for i in range(H):
        for j in range(W):
            print(field[i][j], end='')
        print()
    