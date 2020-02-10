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
                
                    if :
                        overlap = xArr[j] + 10 - xArr[i] + yArr[j] + 10 - yArr[i]
                    