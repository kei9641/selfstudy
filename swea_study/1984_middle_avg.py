T = int(input())
for tc in range(T):
    numbers = list(input().split())
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].strip(' '))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    if sum(numbers) % 8 >= 4:
        print('#{} {}'.format(tc+1, sum(numbers)//8 + 1))
    else:
        print('#{} {}'.format(tc+1, sum(numbers)//8))