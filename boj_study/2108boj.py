N = int(input())
sumN = 0
cnt = {}
maxCnt = 0
modes = []
numbers = []
for _ in range(N):
    number = int(input())
    sumN += number
    if number in cnt:
        cnt[number] += 1
        if cnt[number] == maxCnt:
            modes.append(number)
        elif cnt[number] > maxCnt:
            maxCnt = cnt[number]
            modes = [number]
    else:
        cnt[number] = 1
        if maxCnt == 1:
            modes.append(number)
        elif maxCnt < 1:
            maxCnt = cnt[number]
            modes = [number]
    numbers.append(number)
numbers = sorted(numbers)

# 1. 산술평균
means = round(sumN/N)
print(means)

# 2. 중앙값
median = numbers[N//2]
print(median)

# 3. 최빈값
modes = sorted(modes)
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 4. 범위
midRange = numbers[-1] - numbers[0]
print(midRange)