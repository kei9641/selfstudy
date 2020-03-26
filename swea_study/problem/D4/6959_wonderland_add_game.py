T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input()))
    turn = 0
    while len(number) != 1:
        if number[-1] + number[-2] < 10:
            number[-2] = number[-1] + number[-2]
            number.pop()
        else:
            number[-2], number[-1] = (number[-1] + number[-2])//10, (number[-1] + number[-2])%10
        turn += 1
    if turn % 2 == 0:
        print('#{} B'.format(tc))
    else:
        print('#{} A'.format(tc))