from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
put = deque([0 for _ in range(N)])
step = 0

while 1:
    step += 1

    # 1번 동작
    belt.rotate(1)
    put.rotate(1)
    if put[N-1]:
        put[N-1] = 0
    
    # 2번 동작
    for i in range(N-1, -1, -1):
        if put[i] and put[i+1] == 0 and belt[i+1] > 0:
            put[i], put[i+1] = put[i+1], put[i]
            belt[i+1] -= 1
            if belt[i+1] == 0:
                K -= 1
    if put[N-1]:
        put[N-1] = 0

    # 3번 동작
    if put[0] == 0 and belt[0] > 0:
        put[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            K -= 1

    # 4번 동작
    if K <= 0:
        break

print(step)