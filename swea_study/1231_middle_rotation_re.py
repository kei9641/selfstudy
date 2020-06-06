from collections import deque

T = 1
for tc in range(1, T+1):
    q = deque()
    N = int(input())
    words = ['' for _ in range(N+1)]
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    for _ in range(N):
        S = list(input().split())
        L = len(S)
        if L == 4:
            tree[int(S[0])][0] = int(S[2])
            tree[int(S[0])][1] = int(S[3])
            tree[int(S[2])][2] = int(S[0])
            tree[int(S[3])][2] = int(S[0])
        elif L == 3:
            tree[int(S[0])][0] = int(S[2])
            tree[int(S[2])][1] = int(S[0])
        words[int(S[0])] = S[1]
    visited = [0 for _ in range(N+1)]
    result = ''
    q.append(1)
    while q:
        if len(result) == N+1:
            break
        node = q.popleft()
        if node == 0:
            break
        # 왼쪽 노드를 가지고 방문하지 않았다면
        left = tree[node][0]
        right = tree[node][1]
        if left and visited[left] == 0:
            q.append(left)
        else:
            result += words[node]
            visited[node] = 1
            # 오른쪽 노드를 가지고 방문하지 않았다면
            if right and visited[right] == 0:
                q.append(right)
            else:
                q.append(tree[node][2])
    print(result)

