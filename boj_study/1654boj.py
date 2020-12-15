K, N = map(int, input().split())
tree = [int(input()) for _ in range(K)]

l, h = 1, max(tree)
while l <= h:
    cut = 0
    mid = (l+h) // 2

    for i in range(K):
        cut += tree[i] // mid

    if cut < N:
        h = mid-1
    else:
        l = mid+1
print(l-1)