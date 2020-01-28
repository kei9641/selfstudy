# 1002번

T = int(input())
result = list()

for test_case in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    r_sum = r2 + r1
    r_sub = abs(r2 - r1)
    if distance == 0:  # 두 좌표가 같은 경우
        if r1 == r2:   # 반지름이 같은 경우(두 원은 동일)
            result.append(-1)  # 가능한 위치의 개수 : 무한대
        else:          # 반지름이 다른 경우(두 원은 만나지 않음)
            result.append(0)   # 가능한 위치의 개수 : 0
    else:                                           # 두 좌표가 다른 경우
        if distance == r_sum or distance == r_sub:  # 두 원이 외접 or 내접
            result.append(1)
        elif distance < r_sum and distance > r_sub:  # 두 원이 겹치는 경우
            result.append(2)
        else:                                       # 두 원이 만나지 않는 경우
            result.append(0)

for i in range(T):
    print(result[i])