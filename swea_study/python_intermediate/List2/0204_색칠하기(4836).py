import sys
sys.stdin = open('색칠하기.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    area = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for n in range(N):
        if area[n][-1] == 2: # 빨강이면 
            for x in range(area[n][0], area[n][2]+1):
                for y in range(area[n][1], area[n][3]+1):
                    if arr[x][y] == 1:
                        count += 1
                    arr[x][y] = 2
        if area[n][-1] == 1: # 파랑이면
            for x in range(area[n][0], area[n][2]+1):
                for y in range(area[n][1], area[n][3]+1):
                    if arr[x][y] == 2:
                        count += 1
                    arr[x][y] = 1
 
    print('#{} {}'.format(tc+1, count))

