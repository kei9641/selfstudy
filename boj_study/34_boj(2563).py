N = int(input())
paper = [[0]*101 for _ in range(101)]
blackArea = 0
for t in range(N):
    A, B = map(int, input().split())
    for x in range(B, B+10):
        for y in range(A, A+10):
            if not paper[x][y] == 1:
                blackArea += 1
                paper[x][y] = 1
print(blackArea)