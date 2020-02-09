arr = []
for _ in range(3):
    arr.append(list(input().split()))
for x in range(3):
    for y in range(5):
        print(arr[x][y].lower(), end=" ")
    print()
