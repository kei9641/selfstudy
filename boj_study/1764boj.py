N, M = map(int, input().split())

noListen = set()
for _ in range(N):
    noListen.add(input())

noSee = set()
for _ in range(M):
    noSee.add(input())

results = list(noListen & noSee)
results = sorted(results)

print(len(results))
for result in results:
    print(result)