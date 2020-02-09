L = int(input())
N = int(input())
expectMax = 0
realMax = 0
cake = [0] * L
for i in range(1, N+1):
    P, K = map(int, input().split())
    if expectMax < K - P:
        expectMax = K - P
        expect = i
    for j in range(P-1, K):
        if cake[j] == 0:
            cake[j] = i
for people in range(1, N+1):
    if cake.count(people) > realMax:
        realMax = cake.count(people)
        real = people
print(expect)
print(real)
