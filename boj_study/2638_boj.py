import sys
sys.stdin = open('tc1.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인덱스 벗어남 방지
def isWall(x, y):
    if 0 <= x < N and 0 <= y < M:
        return False
    return True

# 외부 공기이면 2로 바꾸기
def inout(x, y):
    cheese[x][y] = 2
    # print(x,y)
    for n in range(4):
        if isWall(x+dx[n], y+dy[n]) == False:
            if cheese[x+dx[n]][y+dy[n]] == 0:
                inout(x+dx[n], y+dy[n])

N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))

# 총 치즈 수
cnt = 0
for i in range(N):
    cnt += cheese[i].count(1)
# print(cnt)

# 녹은 치즈 위치(초기값은 가장자리 위치)
melt = []
for n in range(M):
    melt.append(0)
    melt.append(n)
    if N != 1:
        melt.append(N-1)
        melt.append(n)
for n in range(N):
    if n != 0 and n != N-1:
        melt.append(n)
        melt.append(0)
        if M != 1:
            melt.append(n)
            melt.append(M-1)

hour = 0 # 치즈가 다 녹는데 걸린 시간
# 아직 치즈가 다 안 녹았으면
while cnt != 0:
    # 외부 공기 체크
    for i in range(0, len(melt), 2):
        # 체크한 위치가 외부공기가 아니면 확인
        if cheese[melt[i]][melt[i+1]] == 0:
            inout(melt[i], melt[i+1])
    # 외부공기 체크 후 리셋
    melt = [] 
    for x in range(N):
        for y in range(M):
            # 치즈가 있는 위치이면 
            if cheese[x][y] == 1:
                air = 0 # 해당 치즈에 닿은 외부 공기의 수
                # 사방에 외부 공기와 접촉하면 air 증가
                for n in range(4):
                    if isWall(x+dx[n], y+dy[n]) == False:
                        if cheese[x+dx[n]][y+dy[n]] == 2:
                            air += 1
                    else:
                        air += 1
                # 외부 공기와 접촉한 면이 2이상이면
                if air >= 2:
                    # 총 치즈 수 감소 
                    cnt -= 1
                    # 녹은 치즈의 위치 저장
                    melt.append(x)
                    melt.append(y)
                    # 치즈를 없애기
                    cheese[x][y] = 0
    # 조건에 해당하는 치즈가 다 녹으면 hour 증가
    hour += 1
print(hour)
# print(100, 100)
# a = [1] * 100
# for _ in range(100):
#     print(*a)