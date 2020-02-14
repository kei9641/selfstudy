T = 10
for tc in range(T):
    number = int(input())
    arr = []
    max_num = 0

    for _ in range(100):
        a = list(map(int, input().split()))
        arr.append(a)
    for i in range(100):
        row, column, diagonal, diagonal_con = 0, 0, 0, 0
        for j in range(100):
            row += arr[i][j]
            column += arr[j][i]
            if i == j:
                diagonal += arr[i][j]
            if i == 99 - j:
                diagonal_con += arr[i][j]
        if max_num < row:
            max_num = row
        if max_num < column:
            max_num = column
        if max_num < diagonal:
            max_num = diagonal
        if max_num < diagonal_con:
            max_num = diagonal_con
    print('#{} {}'.format(number, max_num))