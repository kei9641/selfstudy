numbers = list(map(int, input().split()))
count = 0
for number in numbers:
    if number == 0:
        break
    if number % 5 and number % 3:
        count += 1
print(count)
