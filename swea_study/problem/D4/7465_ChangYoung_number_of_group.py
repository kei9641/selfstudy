T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    member = list(range(1, N+1))
    group = []
    result = 0
    for _ in range(M):
        a = list(map(int, input().split()))
        if len(a) == 2:
            if a[0] in member:
                group.append(a[0])
            if a[1] in member and a[1] not in group:
                member.remove(a[1])
    print(member, group)
    # number = group.count(1)+group.count(0)
    # if group.count(2) == 1:
    #     number -= 1
    # elif group.count(2) == 1:
    #     number -= 1
     
    # print('#{} {}'.format(tc, ))
   