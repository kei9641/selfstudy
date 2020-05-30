from collections import deque

q = deque()
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 초대받은 학생 
    invited = [0 for _ in range(N+1)]
    # 친구 관계 저장
    friends = [[] for _ in range(N+1)]
    # 상원이의 친한 친구
    best_friends = []
    for _ in range(M):
        a, b = map(int, input().split())
        if a == 1:
            best_friends.append(b)
            invited[b] = 1
        elif b == 1:
            best_friends.append(a)
            invited[a] = 1
        else:
            friends[a].append(b)
            friends[b].append(a)
    # 친한 친구의 친한 친구
    for bf in best_friends:
        for friend in friends[bf]:
            if invited[friend] == 0:
                invited[friend] = 1

    print('#{} {}'.format(tc, invited.count(1)))