T = int(input())
for tc in range(1, T+1):
    A, B = map(list, input().split())
    check = [[0 for _ in range(len(B))] for _ in range(len(A))]
    for i 