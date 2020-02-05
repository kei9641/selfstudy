nums = list(map(int, input().split()))
cnt5 = 0
cnt3 = 0
for i in range(10):
    if nums[i] % 3 == 0:
        cnt3 += 1
    if nums[i] % 5 == 0:
        cnt5 += 1
print('Multiples of 3 : {}'.format(cnt3))
print('Multiples of 5 : {}'.format(cnt5))