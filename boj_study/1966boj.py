from collections import deque

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    documents = deque()
    data = list(map(int, input().split()))
    for i in range(N):
        documents.append((i, data[i]))

    done = 0
    while documents:
        pos, doc = documents.popleft()

        for j in range(len(documents)):
            if documents[j][1] > doc:
                documents.append((pos, doc))
                break
        else:
            done += 1
            if pos == M:
                break
    print(done)
