X = int(input())

one = [0 for _ in range(X+1)]
for n in range(2, X+1):
    one[n] = one[n-1] + 1

    if n % 2 == 0 and  one[n] > one[n//2] + 1:
        one[n] = one[n//2] + 1
    if n % 3 == 0 and one[n] > one[n//3] + 1:
        one[n] = one[n//3] + 1

print(one[X])