N = int(input())
switch = list(map(int, input().split()))
T = int(input())
for tc in range(T):
    gender, num = map(int, input().split())
    if gender == 1:
        idx = num-1
        while idx < N:
            if switch[idx] == 0:
                switch[idx] = 1
            elif switch[idx] == 1:
                switch[idx] = 0
            idx += num

    elif gender == 2:
        n = 0
        idx = num-1
        while idx-n >= 0 and idx+n < N:
            if switch[idx-n] == switch[idx+n]:
                if switch[idx-n] == 0:
                    switch[idx-n] = 1
                    switch[idx+n] = 1
                elif switch[idx-n] == 1:
                    switch[idx-n] = 0
                    switch[idx+n] = 0
            else:
                break
            n += 1
for i in range(len(switch)):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()