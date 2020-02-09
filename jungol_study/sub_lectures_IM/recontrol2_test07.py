sum_arr = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        sum_arr[i][j] = i + j + 2
    print(*sum_arr[i])
