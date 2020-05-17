def cal():
    idx = 0
    while num[idx] != []:
        for i in range(len(num[idx])):
            num1 = num[idx][i]+1
            if num1 == M:
                return idx+1
            elif 0 < num1 <= 1000000 and visit[num1] == 0:
                num[idx+1].append(num1)
                visit[num1] = 1
            num2 = num[idx][i]*2
            if num2 == M:
                return idx+1
            elif 0 < num2 <= 1000000 and visit[num2] == 0:
                num[idx+1].append(num2) 
                visit[num2] = 1
            num3 = num[idx][i]-1
            if num3 == M:
                return idx+1
            elif 0 < num3 <= 1000000 and visit[num3] == 0:
                num[idx+1].append(num3) 
                visit[num3] = 1
            num4 = num[idx][i]-10
            if num4 == M:
                return idx+1
            elif 0 < num4 <= 1000000 and visit[num4] == 0:
                num[idx+1].append(num4) 
                visit[num4] = 1
        idx += 1

num = [[] for _ in range(1000001)]
visit = [0 for _ in range(1000001)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num[0].append(N)
    visit[N] = 1
    cnt = cal()
    print('#{} {}'.format(tc, cnt))