T = int(input())
for tc in range(T):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))
    sdoku = True
    for i in range(9):
        for j in range(9): 
            for n in range(1, 8-j): # 가로 줄
                if puzzle[i][j] == puzzle[i][j+n]:
                    sdoku = False
                    break
   
            for m in range(1, 8-j): # 세로 줄
                if puzzle[j][i] == puzzle[j+m][i]:
                    sdoku = False
                    break

            if sdoku == False:
                break
        if sdoku == False:
            break

    for x in range(0, 9, 3): # 칸
        for y in range(0, 9, 3):
            for areaX in range(x, x+3):
                for areaY in range(y, y+3):
                    if x == areaX or y == areaY:
                        continue
                    else:
                        if puzzle[x][y] == puzzle[areaX][areaY]:
                            sdoku = False
                if sdoku == False:
                    break        
            if sdoku == False:
                break     
        if sdoku == False:
            break
        
    if sdoku == True:
        print('#{} {}'.format(tc+1, 1))
    elif sdoku == False:
        print('#{} {}'.format(tc+1, 0))