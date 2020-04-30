import sys
sys.stdin = open('1.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

decode = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    message = [list(input()) for _ in range(N)]
    hex_code = []
    bin_code = []
    code = []
    cal = 0
    result = 0
    for x in range(N):
        for y in range(M):
            if message[x][y] != '0':
                if x == 0 or (message[x-1][y] )

