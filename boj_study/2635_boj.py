N = int(input())
maxLen = 0
for num in range(N, 0 , -1):
    minus = [N, num]
    i = 0
    while minus[i] - minus[i+1] >= 0:
        minus.append(minus[i] - minus[i+1])
        i += 1
    if len(minus) > maxLen:
        maxLen = len(minus)
        maxMinus = minus[:]
print(maxLen)
print(*maxMinus)
