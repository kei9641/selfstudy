arr = list(map(int, input().split()))
evenArr = arr[1::2]
oddArr = arr[::2]
print('sum : {}'.format(sum(evenArr)))
print('avg : {0:.1f}'.format(sum(oddArr)/len(oddArr)))