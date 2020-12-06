import sys

N, S = map(int, sys.stdin.readline().split())
A = [0]
sumNum = 0
for num in sys.stdin.readline().split():
    sumNum += int(num)
    A.append(sumNum)

start, end = 0, 1
result = 100001
while start != N:
    if result == 1:
        break
    if A[end] - A[start] >= S:
        if end - start < result:
            result = end - start
        start += 1
    elif end < N:
        end += 1
    else:
        start += 1


if result == 100001:
    result = 0

print(result)
        