T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = 0
    for _ in range(K):
        idx += M
        if idx == len(arr):
            arr.append(arr[-1]+arr[0])
        else:
            if idx > len(arr):
                idx -= len(arr)
            arr.insert(idx, arr[idx-1]+arr[idx])
    result = arr[-10:]
    print('#{}'.format(tc), end=" ")
    result.reverse()
    print(*result)