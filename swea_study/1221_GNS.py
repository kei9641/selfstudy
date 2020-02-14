T = int(input())
for tc in range(T):
    test_case, n = input().split()
    N = int(n)
    differNum = list(input().split())
    dicNum = {
        "ZRO": 0,
        "ONE": 0, 
        "TWO": 0, 
        "THR": 0, 
        "FOR": 0, 
        "FIV": 0, 
        "SIX": 0, 
        "SVN": 0, 
        "EGT": 0, 
        "NIN": 0
    }
    for num in differNum:
        dicNum[num] += 1
    print('#{}'.format(tc+1))
    for key, val in dicNum.items():
        print((key + ' ') * val, end='')
    print()