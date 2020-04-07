def sqrt(two, three):
    for n in range(two):
        for m in range(three):
            if 2**n - 3**m == gap:
                return n
            elif 2**n + 3**m == gap:
                return n
T = int(input())
for tc in range(1, T+1):
    binary = input()
    len2 = len(binary)
    ternary = input()
    len3 = len(ternary)
    binary = int(binary, 2)
    ternary = int(ternary, 3)
    gap = ternary-binary
    n = sqrt(len2, len3)
    result = binary + 2**n
    print('#{} {}'.format(tc, result))