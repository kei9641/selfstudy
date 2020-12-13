dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fields = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fields[0][r-1][c-1] = [m, s, d, 1]

def move(t0, t1, x0, y0, m0, s0, d0, c0):
    x = (x0 + (dx[d0] * s0)) % N
    y = (y0 + (dy[d0] * s0)) % N
    
    if fields[t1][x][y]:
        m1, s1, d1, c1 = fields[t1][x][y]
        m = m0 + m1
        s = s0 + s1
        if d1 == 10:
            d = 10
        else:
            if (d0 + d1) % 2:
                d = 10
            elif d0 % 2:
                d = 9
            else:
                d = 8
        c = c0 + c1
        fields[t1][x][y] = [m, s, d, c]
        fields[t0][x0][y0] = 0
        if (x, y) not in merge:
            merge.append((x, y))
    else:
        fields[t1][x][y] = [m0, s0, d0, c0]
        fields[t0][x0][y0] = 0

turn = 1
merge = []
while turn <= K:
    for x0 in range(N):
        for y0 in range(N):
            if turn % 2:
                t0, t1 = 0, 1
            else:
                t0, t1 = 1, 0
            if fields[t0][x0][y0]:
                m0, s0, d0, c0 = fields[t0][x0][y0]

                if d0 < 8:
                    move(t0, t1, x0, y0, m0, s0, d0, c0)
                elif d0 == 10:
                    for d in [1, 3, 5, 7]:
                        move(t0, t1, x0, y0, m0, s0, d, 1)
                else:
                    for d in [0, 2, 4, 6]:
                        move(t0, t1, x0, y0, m0, s0, d, 1)
    while merge:
        x0, y0 = merge.pop()
        m0, s0, d0, c0 = fields[t1][x0][y0]
        m, s, c = m0 // 5,  s0 // c0, 4

        if m:
            fields[t1][x0][y0] = [m, s, d0, c]
        else:
            fields[t1][x0][y0] = 0

    turn += 1
    
result = 0
for i in range(N):
    for j in range(N):
        if K % 2:
            t = 1
        else:
            t = 0

        if fields[t][i][j]:
            result += (fields[t][i][j][0] * fields[t][i][j][3])

print(result)
