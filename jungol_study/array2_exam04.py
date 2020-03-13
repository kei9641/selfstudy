arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
result = 0
for i in range(len(arr)):
    print(*arr[i])
    result += sum(arr[i])
print(result)