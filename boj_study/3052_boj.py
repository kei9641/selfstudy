remain = []
for _ in range(10):
    A = int(input())
    remain.append(A%42)
print(len(set(remain)))