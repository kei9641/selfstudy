def generate(m):
    if m == 6:
        m = 1
    if arr[0] - m < 0:
        arr.append(0)
        arr.pop(0)
        return
    arr.append(arr[0]-m)
    arr.pop(0)
    generate(m+1)

T = 10
for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    generate(1)
    print('#{} '.format(tc),end='')
    print(*arr)