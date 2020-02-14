T = int(input())
for tc in range(T):
    num1, num2 = map(int, input().split())

    def cal(x, y):
        result = (((x+y-1) * (x+y-2)) // 2) + x
        return result

    def axisPosition(num):
        for i in range(0, 10001):
            if cal(i, 1) < num <= cal(i+1, 1):
                move = cal(i+1, 1) - num
                x = i - move + 1
                y = move + 1
        return x, y

    x1, y1 = axisPosition(num1)
    x2, y2 = axisPosition(num2)

    print('#{} {}'.format(tc+1, cal(x1+x2, y1+y2)))