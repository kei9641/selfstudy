C, R = map(int, input().split())
row = [0, R]
column = [0, C]
T = int(input())
for tc in range(T):
    line, number = map(int, input().split())
    if line == 0:
        row.append(number)
    elif line == 1:
        column.append(number)
row.sort()
column.sort()
rSize = []
cSize = []
for i in range(1, len(row)):
    rSize.append(row[i]-row[i-1])
for i in range(1, len(column)):
    cSize.append(column[i]-column[i-1])

print(max(rSize) * max(cSize))
