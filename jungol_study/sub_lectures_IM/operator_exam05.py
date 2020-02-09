minsu = list(map(int, input().split()))
giyeong = list(map(int, input().split()))
result = True
for i in range(2):
    if minsu[i] <= giyeong[i]:
        result = False
print(result)
