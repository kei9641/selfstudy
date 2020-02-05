num = int(input())
if num <= 100:
    sum_num = 0
    while num > 0:
        sum_num += num
        num -= 1
    print(sum_num)

