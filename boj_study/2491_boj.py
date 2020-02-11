N = int(input())
progression = list(map(int, input().split()))
count = 1
maxLength = 1 # 0이면 안됨!!!!!!!!!!!!
for i in range(1, N):
    if progression[i-1] <= progression[i]:
        count += 1
    else:
        count = 1
    if maxLength < count:
        maxLength = count
count = 1
for i in range(1, N):
    if progression[i-1] >= progression[i]:
        count += 1
    else:
        count = 1
    if maxLength < count:
        maxLength = count
print(maxLength)
