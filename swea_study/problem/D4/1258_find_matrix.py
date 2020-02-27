import sys
sys.stdin = open('find_matrix.txt')

def find_container():
    global count
    for x in range(N):
        for y in range(N):
            if matrix[x][y] != 0 and visited[x][y] == 0:
                count += 1
                measure(x, y)
    return count

def measure(x0, y0):
    global count
    for x in range(x0, N):
        if matrix[x][y0] == 0:
            x -= 1
            break
    
    for y in range(y0, N):
        if matrix[x0][y] == 0:
            y -= 1
            break
    for i in range(count-1):
        if (x-x0+1)*(y-y0+1) < size[i]:
            size.insert(i, (x-x0+1)*(y-y0+1))
            row.insert(i, x-x0+1)
            column.insert(i, y-y0+1)
            visited_check(x, x0, y, y0)
            return
        elif (x-x0+1)*(y-y0+1) == size[i]:
            if (x-x0+1) < row[i]:
                size.insert(i, (x-x0+1)*(y-y0+1))
                row.insert(i, x-x0+1)
                column.insert(i, y-y0+1)
                visited_check(x, x0, y, y0)
                return
    size.append((x-x0+1)*(y-y0+1))
    row.append(x-x0+1)
    column.append(y-y0+1)
    visited_check(x, x0, y, y0)

def visited_check(x, x0, y, y0):
    for i in range(x0, x+1):
        for j in range(y0, y+1):
            visited[i][j] = 1

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    row = []
    column = []
    size = []
    count = 0
    count = find_container()
    print('#{} {}'.format(tc+1, count),end=' ')
    for i in range(count):
        print(row[i], column[i], end=' ')
    print()
