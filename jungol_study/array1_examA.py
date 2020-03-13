n = int(input())
scores = list(map(int, input().split()))
scores.sort()
scores.reverse()
for i in range(n):
    print(scores[i])