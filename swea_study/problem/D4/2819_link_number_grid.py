result = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def link(x, y):
    global number
    if len(number) == 7:
        if number not in sevenNum:
            sevenNum.append(number)
        return
    for n in range(4):
        if 0 <= x+dx[n] < 4 and 0 <= y+dy[n] < 4:
            number += grid[x+dx[n]][y+dy[n]]
            link(x+dx[n], y+dy[n])
            number = number[:-1]

T = int(input())
for tc in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]
    sevenNum = []
    for x in range(4):
        for y in range(4):
            number = grid[x][y]
            link(x, y)
    result.append(len(sevenNum))

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))


# list를 append 후 해당 list를 변경하면 append 값도 함께 바뀜