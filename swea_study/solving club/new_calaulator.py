import sys
sys.stdin = open('new_calculation.txt')

T = int(input())
for tc in range(T):
    num1, num2 = map(int, input().split())

    def cal(x, y):
        result = int(((x+y-1)*(x+y-2)/2)+x)
        return result
    idx = 1
    while 1:
        if cal(idx, 1) < num1 <= cal(idx+1, 1):
            y1 = cal(idx+1, 1) - num1
            x1 = idx + 1 - y1
            break
        idx += 1
    idx = 1
    while 1:
        if cal(idx, 1) < num2 <= cal(idx+1, 1):
            y2 = cal(idx+1, 1) - num2
            x2 = idx + 1 - y2
            break
        idx += 1

    print('#{} {}'.format(tc+1, cal(x1+x2, y1+y2)))