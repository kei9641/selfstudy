T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    complete = 0
    oven = [0] * (N+1)
    number = 0
    cheese = [0] * (N+1)
    # 마지막 피자가 남을 때까지 오븐을 돌리자
    while complete != M-1:
        # 남은 피자를 비어있는 오븐에 넣자
        if oven[0] == 0 and number < M:
            oven[0] = pizza[number]
            cheese[0] = number
            number += 1
        # 오븐에 든 피자의 치즈를 녹이자
        if oven[0] != 0:
            oven[0] //= 2
            if oven[0] == 0:
                complete += 1
        # 오븐에 든 피자의 돌리자
        oven.insert(-1, oven.pop(0))
        cheese.insert(-1, cheese.pop(0))
        # print(oven, cheese)
    for i in range(N):
        if oven[i] != 0:
            idx = cheese[i]+1
    
    print('#{} {}'.format(tc, idx))
