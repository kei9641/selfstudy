number = int(input())
count = 0
for num in range(number+1):
    if num % 5 == 0:
        count += num
print(count)