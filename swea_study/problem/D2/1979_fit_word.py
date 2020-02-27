T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        row = 0
        column = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                row = 0
            if puzzle[j][i] == 0:
                column = 0
            if puzzle[i][j] == 1:
                row += 1
            if puzzle[j][i] == 1:
                column += 1
            if row == K:
                count += 1
            if column == K:
                count += 1
            if row == K+1:
                count -= 1
            if column == K+1:
                count -= 1
    print('#{} {}'.format(tc+1, count))