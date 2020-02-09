arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == 999:
        break
print('max : {}'.format(max(arr[:i])))
print('min : {}'.format(min(arr[:i])))
