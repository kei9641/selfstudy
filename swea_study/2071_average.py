T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))

    print('#{} {}'.format(tc + 1, round(sum(nums)/len(nums))))