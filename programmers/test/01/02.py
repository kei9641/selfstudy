def solution(N, stages):
    answer = [0 for _ in range(N)]
    playing = [0 for _ in range(N)]
    failure = [0 for _ in range(N)]
    visited = [0 for _ in range(N)]
    player = len(stages)
    for stage in stages:
        if stage-1 < N:
            playing[stage-1] += 1
    for i in range(N):
        failure[i] = playing[i] / player
        player -= playing[i]
    storage = failure[:]
    failure.sort(reverse=True)
    for i in range(N):
        for j in range(N):
            if visited[j] == 0 and failure[i] == storage[j]:
                answer[i] = j+1
                visited[j] = 1
                break
    return answer