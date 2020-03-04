def taste():
    global A, B, minGap
    A, B = 0, 0
    ingreB = []
    # 전체 재료 중 a의 재료가 아닌 재료 ingreB
    for n in range(N):
        if n not in ingreA:
            ingreB.append(n)
    # a의 맛 계산 A
    for x in ingreA:
        for y in ingreA:
            # 대각선 윗부분만 계산
            if x < y:
                A += synergy[x][y]
    # b의 맛 계산 B
    for x in ingreB:
        for y in ingreB:
            # 대각선 윗부분만 계산
            if x < y:
                B += synergy[x][y]
    # (결과값 저장) a, b 맛의 차의 최소값 minGap
    if minGap > abs(A - B):
        minGap = abs(A - B)
    
def select(n, k):
    # (탈출조건) 전체 N개 중 반을 골랐으면 taste() 호출
    if n == k:
        taste()
        return
    # 전체 중 반을 선택 ingreA
    for i in range(N):
        # 저장된 값보다 큰 값만 append (중복 제거용)
        if len(ingreA) == 0 or i > ingreA[-1]:
            ingreA.append(i)
            select(n+1, k)
            ingreA.pop()

result = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    # 대각선을 기준으로 [x][y]와 [y][x]를 더함
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