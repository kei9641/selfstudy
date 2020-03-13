arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == -1:
        break
if i >= 3:
    for j in range(i-3, i):
        print(arr[j], end=' ')
else:
    for j in range(i):
        print(arr[j], end=' ')