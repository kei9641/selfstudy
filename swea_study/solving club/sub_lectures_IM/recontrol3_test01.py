n = int(input())
sumOdd = 0
cntOdd = 0
num = 0
while sumOdd < n:
    if num % 2:
        sumOdd += num
        cntOdd += 1
    num += 1
print('{} {}'.format(cntOdd, sumOdd))
    