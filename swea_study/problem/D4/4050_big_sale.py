T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cloth = list(map(int, input().split()))
    cloth.sort(reverse=True)
    price = 0
    for i in range(N):
        if (i+1) % 3:
            price += cloth[i]
    print('#{} {}'.format(tc, price))