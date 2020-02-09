students = {}
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == 0:
        scores = arr[:i]
        break
    else:
        scores = arr

for n in range(10, -1, -1):
    for score in scores:
        if int(score / 10) == n:
            if n * 10 in students:
                students[n * 10] += 1
            else:
                students[n * 10] = 1
for key in range(100, -1, -10):
    if key in students:
        print('{} : {} person'.format(key, students[key]))
