arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == 0:
        break
newArr = arr[:i]
tens = {}
for n in range(10):
    for num in newArr:
        if num // 10 == n:
            if n in tens:
                tens[n] += 1
            else:
                tens[n] = 1
for key, val in tens.items():
    print('{} : {}'.format(key, val))