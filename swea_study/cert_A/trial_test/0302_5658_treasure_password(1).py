T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    d = N//4
    arr = []
    for i in range(d):
        for j in range(4):
            s = ''
            for p in range(d):
                s += num[(i+j*d+p)%N]
            if int(s, 16) not in arr:
                arr.append(int(s, 16))
    arr.sort(reverse=True)
    print('#{} {}'.format(tc, arr[K-1]))