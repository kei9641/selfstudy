T = int(input())
for tc in range(T):
    N = int(input())
    extraction = ''
    for _ in range(N):
        s, n = input().split()
        num = int(n)
        extraction += s * num
    print('#{}'.format(tc+1))
    for i in range(10, len(extraction), 10):
        print(extraction[i-10:i])
    print(extraction[i:])