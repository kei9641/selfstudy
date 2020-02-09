arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))
totalSum = 0
for x in range(4):
    totalSum += sum(arr[x])
    print(int(sum(arr[x])/2), end=' ')
print()
for y in range(2):
    columnSum = 0
    for x in range(4):
        columnSum += arr[x][y]
    print(int(columnSum/4), end=' ')
print()
print(int(totalSum/8))