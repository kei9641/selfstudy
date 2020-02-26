result = []
T = int(input())
for tc in range(T):
    n = input()
    while len(n) != 1:
        digit_sum = 0
        for i in range(len(n)):
            digit_sum += int(n[i])
        n = str(digit_sum)
    result.append(n)
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))