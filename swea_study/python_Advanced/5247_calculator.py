import time
start_time = time.time()

def cal(n, m):
    global result, cnt
    if result <= cnt:
        return
    if n == m:
        if result > cnt:
            result = cnt
        return
    elif n < m:
        cnt += 1
        cal(n*2, m)
        cal(n+1, m)
        cnt -= 1
    else:
        cnt += 1
        cal(n-10, m)
        cal(n-1, m)
        cnt -= 1
    

# num = [0 for _ in range(10**6)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # num[M] = 1 // 목표값
    cnt = 0
    result = 10**6
    cal(N, M)
    print(result)
print(time.time() - start_time, 'seconds')