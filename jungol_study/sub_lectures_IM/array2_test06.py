passCnt = 0
for _ in range(5):
    scores = list(map(int, input().split()))
    if sum(scores) / len(scores) >= 80:
        print('pass')
        passCnt += 1
    else:
        print('fail')
print('Successful : {}'.format(passCnt))