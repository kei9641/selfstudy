import sys
sys.stdin = open('특별한_정렬.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, N):
        minIdx = i
        maxIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
            if arr[maxIdx] < arr[j]:
                maxIdx = j
        if i % 2 == 0:
            arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
        else:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
    print('#{}'.format(tc+1), end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()
