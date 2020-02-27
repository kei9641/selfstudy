T = int(input())
for tc in range(T):
    numbers = list(map(int, input().split()))
    sums = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                sums.append(numbers[i] + numbers[j] + numbers[k])
    result = list(set(sums))
    result.sort(reverse=True)
    print('#{} {}'.format(tc+1, result[4]))