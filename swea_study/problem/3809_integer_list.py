T = int(input())
for tc in range(T):
    N = int(input())
    integer = []
    while len(integer) != N:
        integer.extend(input().split())

    list_int = ''
    for j in range(N):
        list_int += integer[j]
    i = 0
    while str(i) in list_int:
        i += 1
    print('#{} {}'.format(tc+1, i))

# input이 임의의 줄바꿈으로 구분됨