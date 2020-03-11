T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        s, e = map(int, input().split())
        if s % 2 == 0:
            room.append(s//2-1)
        else:
            room.append(s//2)
        if e % 2 == 0:
            room.append(e//2-1)
        else:
            room.append(e//2)
    corridor = [0]*(max(room)+1)
    turn = 0
    for i in range(0, N*2, 2):
        if room[i] <= room[i+1]:
            for j in range(room[i], room[i+1]+1):
                corridor[j] += 1
                if turn < corridor[j]:
                    turn = corridor[j]
        else:
            for j in range(room[i+1], room[i]+1):
                corridor[j] += 1
                if turn < corridor[j]:
                    turn = corridor[j]

    print('#{} {}'.format(tc, turn))