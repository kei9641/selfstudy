arr = list(map(int, input().split()))
bigArr = []
smallArr = []
for i in arr:
    if i < 100:
        smallArr.append(i)
    else:
        bigArr.append(i)
if smallArr == []:
    maxNum = 100
else:
    maxNum = max(smallArr)
if bigArr == []:
    minNum = 100
else:
    minNum = min(bigArr)
print(maxNum, minNum)