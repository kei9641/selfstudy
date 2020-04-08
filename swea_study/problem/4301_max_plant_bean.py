T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    if M % 4 == 1:
        result = ((M//4)*2+1)*N
    elif M % 4 == 2:
        result = ((M//4)*2+2)*N
    
    # print(result)