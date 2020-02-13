T = int(input())
for tc in range(T):
    num1, num2 = map(int, input().split())
    if num1 >= num2:
        print('#{} {} {}'.format(tc+1, num1//num2, num1%num2))
    else:
        print('#{} {} {}'.format(tc+1, num2//num1, num2%num1))