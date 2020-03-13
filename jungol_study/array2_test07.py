arr = [[1] * 5 for _ in range(5)]
for x in range(1, 5):
    for y in range(1, 5):
        arr[x][y] = arr[x-1][y] + arr[x][y-1]
for i in range(5):
    print(*arr[i])