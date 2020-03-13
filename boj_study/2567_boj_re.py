N = int(input())
arr = []
for _ in range(N):
    arr.extend(list(map(int, input().split())))
xArr = arr[::2]
yArr = arr[1::2]
overlap = 0
for i in range(N):
    for j in range(i+1, N):
        if xArr[i] > xArr[j]:
            if yArr[i] > yArr[j]:
                if xArr[j] + 10 >= xArr[i] and yArr[j] + 10 >= yArr[i]:
                    overlap += xArr[j] + 10 - xArr[i] + yArr[j] + 10 - yArr[i]
            elif yArr[j] > yArr[i]:
                if xArr[j] + 10 >= xArr[i] and yArr[i] + 10 >= yArr[j]:
                    overlap += xArr[j] + 10 - xArr[i] + yArr[i] + 10 - yArr[j]
            else:
                if xArr[j] + 10 >= xArr[i]:
                    overlap += xArr[j] + 10 - xArr[i] + yArr[i]

        elif xArr[j] > xArr[i]:
            if yArr[i] > yArr[j]:
                if xArr[i] + 10 >= xArr[j] and yArr[j] + 10 >= yArr[i]:
                    overlap += xArr[i] + 10 - xArr[j] + yArr[j] + 10 - yArr[i]
            elif yArr[j] > yArr[i]:
                if xArr[i] + 10 >= xArr[j] and yArr[i] + 10 >= yArr[j]:
                    overlap += xArr[i] + 10 - xArr[j] + yArr[i] + 10 - yArr[j]
            else:
                if xArr[i] + 10 >= xArr[j]:
                    overlap += xArr[i] + 10 - xArr[j] + yArr[i]

        else:
            if yArr[i] > yArr[j]:
                if yArr[j] + 10 >= yArr[i]:
                    overlap += xArr[i] + yArr[j] + 10 - yArr[i]
            elif yArr[j] > yArr[i]:
                if yArr[i] + 10 >= yArr[j]:
                    overlap += xArr[i] + yArr[i] + 10 - yArr[j]
            else:
                overlap += xArr[i] + yArr[i]
print(int(40 * N - overlap * 2))
