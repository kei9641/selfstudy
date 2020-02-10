import sys
sys.stdin = open('encoding.txt')

def encode(s):
    num = 0
    if 'A' <= s <= 'Z':
        num = ord(s) - ord('A')
    elif 'a' <= s <= 'z':
        num = ord(s) - ord('a') + 26
    elif '0' <= s <= '9':
        num = ord(s) - ord('0') + 52
    elif s == '+':
        num = 62
    elif s == '/':
        num = 63
    return num

T = int(input())
for tc in range(T):
    strings = input()
    binNums = ''
    for string in strings:
        baseNum = encode(string)
        binNum = "{0:b}".format(baseNum).zfill(6)
        binNums += binNum
    print('#{}'.format(tc+1),end=' ')
    for i in range(0, len(binNums)-7, 8):
        bin8 = ''
        for j in range(8):
            bin8 += binNums[i+j]
        print(chr(int(bin8, 2)), end='')
    print()