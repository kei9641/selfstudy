dice = {}
for key in range(1, 7):
    dice[key] = 0
nums  = list(map(int, input().split()))
for num in nums:
    dice[num] += 1
for key, val in dice.items():
    print('{} : {}'.format(key, val))