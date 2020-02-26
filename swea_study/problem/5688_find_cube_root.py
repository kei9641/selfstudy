T = int(input())
for tc in range(T):
    N = int(input())
    result = -1

    if N < 10**3:
        if N % 2:
            for i in range(1, 10, 2):
                if N == i ** 3:
                    result = i
                    break
        else:
            for i in range(2, 10, 2):
                if N == i ** 3:
                    result = i
                    break
    elif N < 10**6:
        if N % 2:
            for i in range(11, 100, 2):
                if N == i ** 3:
                    result = i
                    break
        else:
            for i in range(10, 100, 2):
                if N == i ** 3:
                    result = i
                    break
    elif N < 10**9:
        if N % 2:
            for i in range((10**2)+1, 10**3, 2):
                if N == i ** 3:
                    result = i
                    break
        else:
            for i in range(10**2, 10**3, 2):
                if N == i ** 3:
                    result = i
                    break
    elif N < 10**12:
        if N % 2:
            for i in range((10**3)+1, 10**4, 2):
                if N == i ** 3:
                    result = i
                    break
        else:
            for i in range(10**3, 10**4, 2):
                if N == i ** 3:
                    result = i
                    break
    elif N < 10**15:
        if N % 2:
            for i in range((10**4)+1, 10**5, 2):
                if N == i ** 3:
                    result = i
                    break
        else:
            for i in range(10**4, 10**5, 2):
                if N == i ** 3:
                    result = i
                    break
    elif N < 10**18:
        if N % 2:
            for i in range((10**5)+1, 10**6, 2):
                if N == i ** 3:
                    result = i
                    break
        else:
            for i in range(10**5, 10**6, 2):
                if N == i ** 3:
                    result = i
                    break
    elif N == 10**18:
        result = 10**6

    print('#{} {}'.format(tc+1, result))
