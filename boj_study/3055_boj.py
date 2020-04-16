from collections import deque

dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]

def isNotWall(x, y):
    return (0 <= x < R) and (0 <= y < C)

R, C = map(int,input().split())
forest = list(input() for _ in range(R))
water = [[-1]*C for _ in range(R)]
visited = [[-1]*C for _ in range(R)]
q = deque()

# 초기 위치 저장
for x in range(R):
    for y in range(C):
        if forest[x][y] == '*':
            # 물부터,, 
            q.append((x, y))
            water[x][y] = 0
        # 고슴도치 출발
        elif forest[x][y] == 'S':
            Sx, Sy = x, y
        # 비버네 집
        elif forest[x][y] == 'D':
            Ex, Ey = x, y

# 물이 퍼지는 것을 체크
while q:
    x, y = q.popleft()
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            # 돌도 아니고 비버 집도 아니면
            if forest[x+dx[n]][y+dy[n]] not in 'DX':
                # 방문하지 않았다면
                if water[x+dx[n]][y+dy[n]] == -1:
                    water[x+dx[n]][y+dy[n]] = water[x][y] + 1
                    q.append((x+dx[n], y+dy[n]))

q.append((Sx, Sy))
visited[Sx][Sy] = 0

# 고슴도치 이동을 체크
while q:
    x, y = q.popleft()
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            # 돌도 아니고 물도 아니면
            if forest[x+dx[n]][y+dy[n]] not in '*X':
                # 방문하지 않았다면
                if visited[x+dx[n]][y+dy[n]] == -1:
                    # 물이 퍼지지 않거나 고슴도치보다 늦게 퍼진다면
                    if water[x+dx[n]][y+dy[n]] == -1 or visited[x][y] + 1 < water[x+dx[n]][y+dy[n]]:
                        visited[x+dx[n]][y+dy[n]] = visited[x][y] + 1
                        q.append((x+dx[n], y+dy[n]))
    
# 도착했다면
if visited[Ex][Ey] == -1:
    print('KAKTUS')
else:
    print(visited[Ex][Ey])

'''
와나 시간초과,,, ㅠㅁㅠ
bfs도전.. => 시간 비교 필요 없어짐, 방문만 체크 필요
=> bfs까진 필요없을듯..?
- 물 먼저
1. queue에 초기값('*') 저장
2. queue에 값이 있으면 꺼내서 사방 확인(while)
2-1. 인덱스 확인(isNotWall)
2-2. XD 있는지 확인
2-3. 이미 물이 차 있는 곳인지 확인(water)
3. queue에 조건 만족하는 사방 값 append
4. 현재 값 +1인 값 저장
queue가 빌 때까지,,
- 다음은 고슴도치
1. ,,('S')
2. ,,
2-2 ,,X*
2-3 ,,(visited)
2-4 물이 퍼진 시간이 고슴도치가 이동한 시간보다 크면
3. ,,
4. ,,
,,
visited[Ex][Ey]에 방문했으면 그 값을 출력 아니면 KAKTUS

'''