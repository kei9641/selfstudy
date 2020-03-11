def generate(n, m):
    global idx
    if m == 6:
        m = 1
    if n == 8:
        n = 0
    if arr[n] - m <= 0:
        arr[n] = 0
        idx = n + 1
        return
    arr[n] -= m
    generate(n+1, m+1)

T = 10
for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    div = min(arr)//15
    for i in range(8):
        arr[i] %= 15*(div-1)
    idx = 0
    generate(0, 1)
    print('#{} '.format(tc),end='')
    print(*(arr[idx:]+arr[:idx]))