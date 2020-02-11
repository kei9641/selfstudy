girls = [0] * 6
boys = [0] * 6
N, K = map(int, input().split())
for _ in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        girls[grade-1] += 1
    elif gender == 1:
        boys[grade-1] += 1
students = boys + girls
countRoom = 0
for num in students:
    while num > 0:
        countRoom += 1
        num -= K
print(countRoom)
