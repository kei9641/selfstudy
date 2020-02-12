'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18

5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
board = []
numbers = []
bingo = 0
for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(6):
    numbers += list(map(int, input().split()))

for idx in range(25):
    for x in range(5):
        for y in range(5):
            if board[x][y] == numbers[idx]:
                board[x][y] = 0
                break

    bingo = 0
    for row in range(5):
        if board[row] == [0, 0, 0, 0, 0]:
            bingo += 1
        if bingo >= 3:
            break

        for column in range(5):
            resultC = True
            if board[column][row] != 0:
                resultC = False
                break
        if resultC == True:
            bingo += 1
        if bingo >= 3:
            break

        resultF = True
        if board[row][row] != 0:
            resultF = False
        if resultF == True:
            bingo += 1
        if bingo >= 3:
            break

        resultR = True
        if board[row][4-row]:
            resultR = False
        if resultR == True:
            bingo += 1
        if bingo >= 3:
            break

    if bingo >= 3:
        break
print(idx+1)

            
