import sys
sys.stdin = open('stringPalindrome.txt')

def palindrome(a):
    result = True
    for i in range(len(a)):
        if a[i] != a[-(i+1)]:
            result = False
    return result


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    strings = []
    for _ in range(N):
        strings.append(input())
    for x in range(N):
        
        start = 0
        end = M
        strings[x][start:end]