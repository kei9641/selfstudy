N, H = map(int, input().split())
suksun = [0] * H # 석순
jongu = [0] * H # 종유석

# 최대 크기 값 저장
for n in range(0, N):
    size = int(input())
    # 석순
    if n % 2 == 0:
        suksun[size-1] += 1
    # 종유석
    else:
        jongu[size-1] += 1

# 전체 크기 값 계산
for i in range(H-1, 0, -1):
    suksun[i-1] += suksun[i]
    jongu[i-1] += jongu[i]

destroy = N # 파괴할 장애물 수
firefly = 1 # 최소 장애물 경로 수

for i in range(H):
    # 경로별 총 장애물 수
    route = jongu[i] + suksun[H-i-1]
    # 총 장애물 수가 최소라면 저장하고 경로 수 리셋
    if route < destroy:
        destroy = route
        firefly = 1
    # 최소 장애물을 지나는 경로라면 경로 수 증가
    elif route == destroy:
        firefly += 1

print(destroy, firefly)

'''
시간 좀 줄이자...
1. 하나씩 훑으면서 크기 값 더하면 시간이 너무 오래걸림..
    => 최대 크기 값만 저장해서 밑에 값에 누적시키기
2. 이중 for문 금지!!! (N*H는 시간초과..)
'''
