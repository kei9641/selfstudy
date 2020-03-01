import sys
sys.stdin = open('treasure_password.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    numbers = list(input())
    passwords = []
    for i in range(N):
        num = '0x'
        for n in range(N//4-1, -1, -1):
            num += numbers[i-n]
        if int(num, 16) not in passwords:
            passwords.append(int(num, 16))
    passwords.sort(reverse=True)
    print('#{} {}'.format(tc+1, passwords[K-1]))
