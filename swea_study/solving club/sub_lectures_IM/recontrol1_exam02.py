nums = list(map(int, input().split()))
odd_cnt = 0
even_cnt = 0 
for num in nums:
    if num == 0:
        break
    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
print('odd : {}'.format(odd_cnt))
print('even : {}'.format(even_cnt))
