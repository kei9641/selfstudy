T = int(input())
for tc in range(T):
    N = int(input())
    enter = []
    check = [0] * N
    for _ in range(N):
        enter.append(int(input()))
    check[0] = 1
    count = 0
    while check != [1] * N:
        count += 1
        for i in range(1, N):
            if check[i] == 0:
                period = enter[i] - 1
                break
        for j in range(1, N):
            if (enter[j] - 1) % period == 0 :
                check[j] = 1
    print('#{} {}'.format(tc+1, count))