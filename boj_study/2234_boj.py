# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상하좌우로 이동할 수 있는 경우
route = [[0, 1, 4, 5, 8, 9, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7], [0, 2, 4, 6, 8, 10, 12, 14], [0, 1, 2, 3, 8, 9, 10, 11]]

# 인덱스 범위 체크
def isNotWall(x, y):
    return (0 <= x < m) and (0 <= y < n)

def dfs(x, y):
    global area
    # 탐색하는 곳에 방 번호(idx)를 저장
    room[x][y] = idx
    # 방 크기를 증가
    area += 1
    # 상하좌우
    for n in range(4):
        # 인덱스가 범위 내면
        if isNotWall(x+dx[n], y+dy[n]):
            # 해당 방향으로 이동 가능하다면(벽이 없으면)
            if castle[x][y] in route[n]:
                # 이동하지 않은 곳이면
                if room[x+dx[n]][y+dy[n]] == 0:
                    # 이동
                    dfs(x+dx[n], y+dy[n])
            # 해당 방향에 벽이 있고, 방 번호가 저장되어 있는 곳이면
            elif room[x+dx[n]][y+dy[n]]:
                # 이웃한 다른 방인지 확인
                if room[x+dx[n]][y+dy[n]] != room[x][y]:
                    # 이웃한 두 방 번호가 저장되어 있지 않으면
                    if (room[x+dx[n]][y+dy[n]], room[x][y]) not in connects:
                        # connect에 추가
                        connects.append((room[x+dx[n]][y+dy[n]], room[x][y]))

n, m = map(int, input().split())
# 입력받은 벽 데이터
castle = [list(map(int, input().split())) for _ in range(m)]
# 통로가 이어져있다면 같은 번호(idx)를 저장(idx는 1부터)
room = [[0 for _ in range(n)] for _ in range(m)]
# 이어져있는 한 공간의 크기를 방 번호에 맞춰서 저장(size[idx])
size = [0]
# 이웃한 방의 번호(idx)를 튜플 형태로 저장
connects = []
# 이웃한 방의 크기를 더한 값을 저장
extends = []
# 방 번호
idx = 1
for x in range(m):
    for y in range(n):
        # 아직 방 번호가 체크되지 않았다면(방문하지않았다면)
        if room[x][y] == 0:
            # 방의 크기를 카운트할 변수
            area = 0
            dfs(x, y)
            # dfs 후 방의 크기(area)를 해당 방 번호(idx)에 저장
            size.append(area)
            # 방 번호 증가
            idx += 1

for connet in connects:
    # 이웃한 방 번호를 언팩킹
    n1, n2 = connet
    # 두 방의 크기를 더하기
    extend = size[n1] + size[n2]
    # 두 방의 크기를 더한 값이 저장되어있지 않으면
    if extend not in extends:
        # extends에 추가
        extends.append(extend)
# 방의 수
print(idx-1)
# 최대 방의 크기
print(max(size))
# 연결했을 때 최대 방의 크기
print(max(extends))
