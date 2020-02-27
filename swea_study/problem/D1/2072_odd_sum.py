T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))
    sumOdd = 0
    for num in nums:
        if num % 2:
            sumOdd += num
    print('#{} {}'.format(tc+1, sumOdd))
