def sqrt(result, three):
    for n in range(1, len(ternary)):
        if abs(result-three) == 3**n or abs(result-three) == (3**n)*2:
            return True                        

T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()
    for i in range(len(binary)-1, 0, -1):
        if binary[i] == '0':
            result = int(binary, 2) + 2**(len(binary)-1-i)
        else:
            result = int(binary, 2) - 2**(len(binary)-1-i)
        if sqrt(result, int(ternary, 3)) == True:
            break

    print('#{} {}'.format(tc, result))