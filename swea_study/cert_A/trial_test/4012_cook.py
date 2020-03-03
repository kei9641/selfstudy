def taste():
    global A, B, minGap
    A, B = 0, 0
    ingreB = []
    for n in range(N):
        if n not in ingreA:
            ingreB.append(n)
    for x in ingreA:
        for y in ingreA:
            if x < y:
                A += synergy[x][y]
    for x in ingreB:
        for y in ingreB:
            if x < y:
                B += synergy[x][y]
    if minGap > abs(A - B):
        minGap = abs(A - B)
    
def select(n, k):
    if n == k:
        taste()
        return
    for i in range(N):
        if len(ingreA) == 0 or i > ingreA[-1]:
            ingreA.append(i)
            select(n+1, k)
            ingreA.pop()

result = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if x < y:
                synergy[x][y] += synergy[y][x]
            else:
                synergy[x][y] = 0
    ingreA = []
    ingreB = []
    minGap = 1000000
    select(0, N//2)
    result.append(minGap)
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))