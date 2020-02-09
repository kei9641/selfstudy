arr = list(map(int, input().split()))
i = 0
while len(arr) < 10:
    arr.append((arr[i] + arr[i+1]) % 10)
    i += 1
print(*arr)