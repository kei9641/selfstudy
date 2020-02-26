T = int(input())
for tc in range(T):
    N = int(input())
    velocity = 0
    distance = 0
    for _ in range(N):
        command = list(map(int, input().split()))
        ctrl = command[0]
        if ctrl != 0:
            accel = command[1]
            if ctrl == 1:
                velocity += accel
            elif ctrl == 2:
                if velocity <= accel:
                    velocity = 0
                else:
                    velocity -= accel
        distance += velocity
    print('#{} {}'.format(tc+1, distance))