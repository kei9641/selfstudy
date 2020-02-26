T = int(input())
for tc in range(T):
    string = input()
    N = len(string)
    line2 = ''
    arr = [[0] * 5 * N for _ in range(5)]
    if len(string) == 1:
        arr[0] = list('..#..')
        arr[1] = list('.#.#.')
        arr[2] = list('#.' + string + '.#')
        arr[3] = list('.#.#.')
        arr[4] = list('..#..')
    else:
        arr[0] = list('..' + ('#...' * (N-1)) + '#..')
        arr[1] = list('.#' * N * 2 + '.')
        line2 += '#.'
        for i in range(N-1):
            line2 += (string[i] + '.#.')
        line2 += (string[-1] + '.#')
        arr[2] = list(line2)
        arr[3] = list('.#' * N * 2 + '.')
        arr[4] = list('..' + ('#...' * (N-1)) + '#..')
        # print(arr)

    for i in range(5):
        for j in range(len(arr[i])):
            print(arr[i][j],end='')
        print()