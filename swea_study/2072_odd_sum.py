'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
'''
T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))
    sumOdd = 0
    for num in nums:
        if num % 2:
            sumOdd += num
    print('#{} {}'.format(tc+1, sumOdd))
