def subsequence(n):
    global result
    if n == N:
        if len(sub)-1 > result:
            result = len(sub)-1
        return
    for i in range(n, N):
        if numbers[i] >= sub[-1]:
            sub.append(numbers[i])
            subsequence(i+1)
            sub.pop()

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    sub = [0]
    result = 0
    subsequence(0)
    print('#{} {}'.format(tc+1, result))
