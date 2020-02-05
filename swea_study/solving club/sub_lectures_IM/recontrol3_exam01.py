numbers = list(map(int, input().split()))
num = []
for number in numbers:
    if number == 0:
        break
    else:
        num.append(number)
print('{} {}'.format(sum(num), int(sum(num)/len(num))))
