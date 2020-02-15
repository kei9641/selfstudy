T = int(input())
for tc in range(T):
    N = float(input())
    number = 0
    binary = ''
    for n in range(1, 15):
        if n == 13:
            binary = 'overflow'
            break
        number += 2**(-n)
        if N > number:
            binary += '1'
        elif N == number:
            binary += '1'
            break
        else:
            binary += '0'
            number -= 2**(-n)
    print('#{} {}'.format(tc+1, binary))