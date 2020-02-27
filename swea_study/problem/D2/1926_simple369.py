N = int(input())
rule = ['3', '6', '9']
for num in range(1, N+1):
    clap = ''
    for i in range(3):
        for j in range(len(str(num))):
            if rule[i] == str(num)[j]:
                clap += '-'
    if clap == '':
        print(num, end=' ')
    else:
        print(clap, end=' ')
