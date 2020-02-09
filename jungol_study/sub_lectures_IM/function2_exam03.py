numbers = list(map(int, input().split()))
absSum = 0
for number in numbers:
    absSum += abs(number)
print(absSum)