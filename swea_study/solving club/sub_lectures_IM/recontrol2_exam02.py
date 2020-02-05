numbers = list(map(int, input().split()))
for num in range(min(numbers), max(numbers)+1):
    print(num, end=' ')