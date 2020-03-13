arr = list(map(int, input().split()))
fiveArr = []
for num in arr:
    if num == 0:
        break
    else:
        if num % 5 ==0:
            fiveArr.append(num)
print('Multiples of 5 : {}'.format(len(fiveArr)))
print('sum : {}'.format(sum(fiveArr)))
print('avg : {0:.1f}'.format(sum(fiveArr)/len(fiveArr)))
