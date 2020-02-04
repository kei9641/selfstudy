cm, kg = map(int, input().split())
check = kg + 100 - cm
print(check)
if check > 0:
    print('Obesity')