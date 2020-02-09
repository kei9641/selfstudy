croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=']
string = input()
wordCnt = 0
dzCnt = 0
for croatian in croatia:
    if croatian in string:
        wordCnt += string.count(croatian)
wordCnt += string.count('z=')
wordCnt -= string.count('dz=')
dzCnt += string.count('dz=')
print(len(string) - wordCnt - dzCnt*2)
