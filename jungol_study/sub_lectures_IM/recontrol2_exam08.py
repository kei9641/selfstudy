row, column = map(int, input().split())
for x in range(row):
    for y in range(column):
        print(((x+1)*(y+1)),end=' ')
    print()