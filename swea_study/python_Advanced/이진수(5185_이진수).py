import sys
sys.stdin = open("이진수(5185_이진수).txt")

T = int(input())
for tc in range(1, T+1):
    d, h = input().split()
    digit = int(d)
    numbers = list(h)
    binary = ''
    for number in numbers:
        if ord('0') <= ord(number) <= ord('9'):
            binary += '{0:b}'.format(int(number)).zfill(4)
        else:
            binary += '{0:b}'.format(ord(number) - ord('A') + 10).zfill(4)
    print('#{} {}'.format(tc, binary))
