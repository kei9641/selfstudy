T = int(input())
for tc in range(T):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        print('#{} {}'.format(tc+1, '>'))
    elif num1 < num2:
        print('#{} {}'.format(tc+1, '<'))
    elif num1 == num2:
        print('#{} {}'.format(tc+1, '='))