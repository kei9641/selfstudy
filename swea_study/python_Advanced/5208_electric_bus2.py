T = int(input())
for tc in range(1, T+1):
    station = list(map(int, input().split()))
    N = station[0]
    goal = N
    cnt = -1
    while 1:
        for i in range(1, goal):
            if goal - i <= station[i]:
                goal = i
                cnt += 1
                break
        else:
            break
    print('#{} {}'.format(tc, cnt))