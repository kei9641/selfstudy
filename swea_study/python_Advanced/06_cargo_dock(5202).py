import sys
sys.stdin = open('cargo_dock.txt')
# start = [20, 17, 23, 4, 8]
# end = [23, 20, 24, 14, 18]

def dfs(idx):
    global count
    if idx == N:
        return
    for i in range(s[idx], e[idx]):
        if times[i] == 0:
            times[i] = 1
        else:
            return
    pre_times = times
    dfs(idx+1)
    times = pre

T = int(input())
for tc in range(T):
    N = int(input())
    start = []
    end = []
    for _ in range(N):
        s, e = map(int, input().split())
        start.append(s)
        end.append(e)
    times = [0 for _ in range(25)]
    dfs(0)