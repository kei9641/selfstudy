T = int(input())
for tc in range(1, T+1):
    sound = input()
    C = []
    R = []
    O = []
    A = []
    K = []
    result = -1
    cnt = 0
    check = True
    flog = 0
    if len(sound) % 5 == 0:
        if sound.count('c') == sound.count('r') == sound.count('o') == sound.count('a') == sound.count('k'):
            for i in range(len(sound)):
                if sound[i] == 'c':
                    C.append(i)
                elif sound[i] == 'r':
                    R.append(i)
                elif sound[i] == 'o':
                    O.append(i)
                elif sound[i] == 'a':
                    A.append(i)
                elif sound[i] == 'k':
                    K.append(i)
            for n in range(len(sound)//5):
                if not C[n] < R[n] < O[n] < A[n] < K[n]:
                    check = False
                    break
            if check == True:
                for j in range(len(sound)):
                    if j in C:
                        flog += 1
                    elif j in K:
                        flog -= 1
                    if result < flog:
                        result = flog
    print('#{} {}'.format(tc, result))
