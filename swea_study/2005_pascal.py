T = int(input())
for tc in range(T):
    N = int(input())
    lines = []
    for turn in range(1, N+1):
        line = [1] * turn
        lines.append(line)
    for x in range(2, len(lines)):
        for y in range(len(lines[x])):
            if y != 0 and y != len(lines[x])-1:
                lines[x][y] = lines[x-1][y-1] + lines[x-1][y]
    
    print('#{}'.format(tc+1))
    for i in range(N):
        print(*lines[i])