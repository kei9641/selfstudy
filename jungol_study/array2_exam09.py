N = int(input())
pascal = []
for line in range(1, N+1):
    pascal.append([1] * line)
for x in range(2, N):
    for y in range(1, x):
        pascal[x][y] = pascal[x-1][y-1] + pascal[x-1][y]
for i in range(N-1, -1, -1):
    print(*pascal[i])