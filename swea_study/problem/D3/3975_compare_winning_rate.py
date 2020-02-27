result = []
T = int(input())
for tc in range(T):
    A, B, C, D = map(int, input().split())
    
    alice_rate = A / B
    bob_rate = C / D
    if alice_rate > bob_rate:
        result.append('ALICE')
    elif alice_rate < bob_rate:
        result.append('BOB')
    else:
        result.append('DRAW')

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))

# 각 테스트케이스마다 출력하면 시간이 더 오래걸림