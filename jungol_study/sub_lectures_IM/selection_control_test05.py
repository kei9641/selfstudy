score1, score2 = map(float, input().split())
if score1 >= 4.0 and score2 >= 4.0:
    print('A')
elif score1 >= 3.0 and score2 >= 3.0:
    print('B')
else:
    print('C')