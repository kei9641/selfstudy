import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isNotWall(x, y):
    return (0 <= x < N) and (0 <= y < M)

# 외부 공기 체크
def inout(x, y):
    cheese[x][y] = -1
    for i in range(4):
        if isNotWall(x+dx[i], y+dy[i]):
            # 외부 공기 사방에 치즈가 있으면 접촉 횟수만큼 증가
            if cheese[x+dx[i]][y+dy[i]] > 0:
                cheese[x+dx[i]][y+dy[i]] += 1
            # 외부 공기이면 dfs 계속
            elif cheese[x+dx[i]][y+dy[i]] == 0:
                inout(x+dx[i], y+dy[i])

# 남은 치즈 체크
def meltCnt():
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 치즈면 cnt 증가
            if cheese[i][j] == 1 or cheese[i][j] == 2:
                cheese[i][j] = 1
                cnt += 1
            else:
                cheese[i][j] = 0
    return cnt

N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))

hour = 0
# 남은 치즈가 있으면 반복
while meltCnt():
    inout(0, 0)
    hour += 1

print(hour)

'''
재귀 횟수 문제......(런타임에러)
import sys
sys.setrecursionlimit(100000)
//메모리 초과는 해결x

위치 체크 대신 전체 탐색 횟수 줄이기,,
<탐색>
1. 외부 공기랑 내부 공기 구분
2. 외부 공기와 치즈의 접촉 횟수 구하기
3. 2 이상 접촉한 치즈 녹이기
4. 남은 치즈 확인
5. 원상태로 구분
치즈가 없을 때까지 1~5 반복 (while 남은 치즈 수 => 4.)
<한 번에 해결할 수 있는 거>
1. & 2. : 외부 공기(-1) 체크하면서 주변에 치즈 있으면 +1
3. & 5. : 0-내부공기, 1 & 2-남은 치즈, 3-녹일 치즈, -1-외부공기
        => 3 & -1 & 0은 0으로, 1 & 2는 1로 바꾸기
'''