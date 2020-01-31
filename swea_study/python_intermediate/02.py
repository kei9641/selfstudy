T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    stations = [0] * (N+1)
    count = 0
    turn = 0
    for charger in chargers:
        stations[charger] = 1
    start = 0
    finish = K
    while finish < N and turn < K:
        
        for i in range(finish, start, -1):
            if stations[i] == True:
                start = finish
                finish += K
                count += 1
                turn = 0
                break
            turn += 1
            finish -= 1
    if turn == K:
        count = 0
    print('#{} {}'.format(tc+1, count))
