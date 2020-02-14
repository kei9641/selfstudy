T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1
    for i in range(N):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            if num >= 10:
                number = str(num)
                for k in range(1, len(number)):
                    if number[k-1] > number[k]:
                        break
                else:
                    if result < num:
                        result = num
    print('#{} {}'.format(tc+1, result))
