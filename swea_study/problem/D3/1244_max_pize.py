def change(n, k):
    global result
    if n == k:
        if result < int(''.join(number)):
            result = int(''.join(number))
        return
    for i in range(len(number)):
        for j in range(len(number)):
            if i < j:
                number[i], number[j] = number[j], number[i]
                change(n+1, k)
                number[i], number[j] = number[j], number[i]
T = int(input())
for tc in range(1, T+1):
    S, N = map(int, input().split())
    number = list(str(S))
    result = 0
    count = [0]*10
    maxNum = sorted(number, reverse=True)
    for i in range(len(number)):
        count[int(number[i])] += 1
    if max(count) > 1 and N >= len(number) - max(count):
        result = ''.join(maxNum)
    elif max(count) == 1 and N >= len(number) - 1:
        for n in range(len(maxNum)):
            idx = number.index(maxNum[n])
            number[idx], number[n] = number[n], number[idx]
            if number == maxNum:
                break
        if (N-n+1) % 2:
            number[-1], number[-2] = number[-2], number[-1]
        result = ''.join(number)
    else:
        change(0, N)
    print('#{} {}'.format(tc, result))