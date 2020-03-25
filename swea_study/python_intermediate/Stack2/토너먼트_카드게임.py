import sys
sys.stdin = open('토너먼트_카드게임.txt')

def partition(l, r):
    if r - l == 1:
        a = l
        b = r
    else:
        a = partition(l, (l+r)//2)
        if (l+r)//2+1 == r:
            b = r
        else:
            b = partition((l+r)//2+1, r)

    return versus(a, b)

def versus(i, j):
    if (battle[i] == 1 and battle[j] == 2) or (battle[i] == 2 and battle[j] == 3) or (battle[i] == 3 and battle[j] == 1):
        return j
    else:
        return i

T = int(input())
for tc in range(T):
    N = int(input())
    battle = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, partition(0, N-1)+1))
