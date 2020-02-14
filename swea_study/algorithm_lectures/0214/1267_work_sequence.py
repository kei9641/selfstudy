import sys
sys.stdin = open('work_sequence.txt')

def dfs(v):
    visited[v] = 1
    sequence.append(v)
    for w in range(1, V+1): 
        if works[w][v] == 1 and visited[w] == 0 and w not in preworks:  # 다음 루트 탐색
            # for i in range(V+1): 
            #     if works[w][i] == 1: # 선행 작업 저장
            #         preworks.append(i)
            #     for j in range(len(preworks)): # 선행 작업 완료 확인
            #         if visited[preworks[j]] == 0: # 미완료된 선행 작업이 있으면 먼저 수행
            #             dfs(preworks[j])
            dfs(w)

for tc in range(10):
    V, E = map(int, input().split())
    works = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    lines = list(map(int, input().split()))
    sequence = []
    preworks = [0 for _ in range(V+1)]

    # 1. 간선 입력
    for n in range(0, E*2, 2):
        works[lines[n+1]][lines[n]] = 1
    for i in range(1, V+1): # 시작점 탐색
        if works[i] == [0]*(V+1):
            dfs(i)
    # for i in range(1, V+1):
    #     for j in range(1, V+1):
    #         if works[i][j] == 1:
    #             preworks.append(i)
                    # dfs(i)
    print(preworks)


    # print('#{}'.format(tc+1),end=' ')
    # print(*sequence)