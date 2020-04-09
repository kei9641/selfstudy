'''
1. 10 9
2. 4995 37
3. 49 6
4. 16212 7991
5. 4938 499034
6. 0 9599
7. 38428 8
8. 42965 10405
9. 5011 807
10. 90151 139427
'''
import sys
sys.stdin = open('tc6.txt')

N, H = map(int, input().split())
obstacle = [] # 장애물 크기
for _ in range(N):
    obstacle.append(int(input()))

destroy = N//2 # 파괴량
firefly = 2 # 최소 파괴 경로의 수 (처음이랑 끝)
# print(destroy, firefly)

bottomstone = []  # 석순의 크기
ceilstone = []  # 종유석의 크기

# 석순, 종유석 나누기
for i in range(N):
    # 석순
    if i % 2 == 0:
        bottomstone.append(obstacle[i])
    # 종유석
    else:
        ceilstone.append(obstacle[i])
# 석순은 오름차순, 종유석은 내림차순
bottomstone.sort()
ceilstone.sort(reverse=True)
# print(bottomstone, ceilstone)

stones = [] # 석순, 종유석 크기의 합
for i in range(N//2):
    stones.append(bottomstone[i] + ceilstone[i])
# print(stones)

space = [] # 남는 공간의 크기
for i in range(N//2):
    space.append(H-stones[i])
# print(space)

route = [0] * H
# 남는 공간이 있다면
if max(space) > 0:
    # 빈 공간만큼 경로에 저장
    for j in range(N//2):
        n = 0
        while space[j] > 0:
            route[bottomstone[j]+n] += 1
            n += 1
            space[j] -= 1
    destroy -= max(route)
    firefly = route.count(max(route))
# 남는 공간이 없다면 
elif max(space) == 0:
    # 최소 파괴 경로의 수 체크
    for j in range(N//2):
        n = 1
        while space[j] < 0:
            route[bottomstone[j]-n] = 1
            n += 1
            space[j] += 1
    firefly = route.count(0)
# max(space) < 0 경우 초기값 출력
# print(route)

print(destroy, firefly)
