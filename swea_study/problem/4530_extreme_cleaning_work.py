def check(d, floor, four):
    # print(d, floor, four)
    for i in range(d):
        if i == d-1:
            if int(floor[i]) > 4:
                # print('a', int(floor[i]) ,i)
                four[i] += 1
                # print(four[i])
        else:
            if int(floor[i]) < 4:
                # print('b 1', int(floor[i]), i)
                four[i] += (int(N[i]) * step[d-1])
                # print(four[i])
            else:
                # print('b 2', int(floor[i]), i)
                # print(int(floor[i]), step[d-1])
                four[i] += (int(floor[i]) * step[d-1] + (10**(d-(i+1))))
                # print(four[i])
        # print(four)


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    step = [0, 1, 19, 271, 3439, 40951, 468559, 5217031, 56953279, 612579511, 6513215599, 68618940391, 717570463519]
    digitA, digitB = len(A), len(B)
    fourA = [0] * digitA
    fourB = [0] * digitB
    check(digitA, A, fourA)
    check(digitB, B, fourB)
    print(fourA)
    print(fourB)