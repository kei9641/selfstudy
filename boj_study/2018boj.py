N = int(input())

count = 1
for i in range(1, N//2+1):
    sumNum = 0
    n = 0
    while sumNum <= N:
        if sumNum == N:
            count +=1
            break
        sumNum += i+n
        n += 1

print(count)