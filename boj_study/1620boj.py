N, M = map(int, input().split())

pockets = {}
for i in range(1, N+1):
    pocketmon = input()
    pockets[str(i)] = pocketmon
    pockets[pocketmon] = i

for _ in range(M):
    quiz = input()
    print(pockets[quiz])