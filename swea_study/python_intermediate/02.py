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
    # while finish < N:
    #     stops = stations[start:finish]
    #     if stops[:-1] == True:
    #         start = finish
    #         finish += K
    #         count += 1
    #     else:
    #         finish -= 1
    while finish < N or turn < K:
        for i in range(finish, start, -1):
            if stations[i] == True:
                start = finish
                finish += K
                count += 1
                break
            else:
                finish -= 1
                turn += 1
                break
    print(count)