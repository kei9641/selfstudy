N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    aMark = [0] * 4
    bMark = [0] * 4
    for i in range(1, A[0]+1):
        aMark[A[i]-1] += 1
    for i in range(1, B[0]+1):
        bMark[B[i]-1] += 1

    for idx in range(3, -1, -1):
        if aMark[idx] > bMark[idx]:
            print('A')
            break
        elif aMark[idx] < bMark[idx]:
            print('B')
            break
    if aMark == bMark:
        print('D')