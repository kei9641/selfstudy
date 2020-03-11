T = 10
for tc in range(1, T+1):
    N = int(input())
    origin = list(input().split())
    M = int(input())
    command = list(input().split())
    idx = 0
    turn = 0
    i = 0
    while i != len(command):
        if command[i] == 'I':
            idx = int(command[i+1])
            turn = int(command[i+2])
        for n in range(1, turn+1):
            origin.insert(idx+(n-1), command[i+2+n])
        i += n+3
    print('#{} '.format(tc),end='')
    print(*origin[:10])
