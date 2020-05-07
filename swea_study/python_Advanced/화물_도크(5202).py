import sys
sys.stdin = open('화물_도크(5202).txt')
# start = [20, 17, 23, 4, 8]
# end = [23, 20, 24, 14, 18]

T = int(input())
for tc in range(T):
    N = int(input())
    start = []
    end = []
    for _ in range(N):
        s, e = map(int, input().split())
        start.append(s)
        end.append(e)
    time = [0 for _ in range(25)]
    visited = [0 for _ in range(N)]
    count = 0
    # n: 작업을 완료하는데 걸리는 시간
    for n in range(1, 25):
        for idx in range(N):
            # 작업을 완료하는 시간이 작은 것부터 반영되지 않은 내용이면
            if end[idx] - start[idx] == n and visited[idx] == 0:
                # check: 신청 시간대에 스케쥴이 있는지 확인 
                check = True
                for i in range(start[idx], end[idx]):
                    # 작업 시간대가 스케쥴에 있으면 False
                    if time[i] == 1:
                        check = False
                # 작업 시간대가 스케쥴에 없으면 
                if check == True:
                    visited[idx] = 1
                    count += 1
                    for i in range(start[idx], end[idx]):
                        time[i] = 1
    print('#{} {}'.format(tc+1, count))