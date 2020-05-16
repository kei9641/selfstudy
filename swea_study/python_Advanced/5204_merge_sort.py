def merge(L):
    global cnt
    if len(L) == 1:
        return L
    left = merge(L[:len(L)//2])
    right = merge(L[len(L)//2:])
    i = 0
    j = 0
    n = 0
    while len(left) - i and len(right) - j:
        if left[i] < right[j]:
            L[n] = left[i]
            i += 1
        else:
            L[n] = right[j]
            j += 1
        n += 1
    if i < len(left):
        L[n:] = left[i:]
    if j < len(right):
        L[n:] = right[j:]
    if left[-1] > right[-1]:
        cnt += 1
    return L

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    a = merge(a)
    print('#{} {} {}'.format(tc, a[N//2], cnt))