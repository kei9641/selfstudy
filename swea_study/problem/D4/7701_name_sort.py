T = int(input())
for tc in range(1, T+1):
    N = int(input())
    names = [[] for _ in range(51)]
    result = []
    for _ in range(N):
        s = input()
        if '\r' in s:
            s = s[:-2]
        names[len(s)].append(s)
    for i in range(51):
        if names[i] != []:
            result += sorted(list(set(names[i])))
    print('#{}'.format(tc))
    for j in range(len(result)):
        print(result[j])