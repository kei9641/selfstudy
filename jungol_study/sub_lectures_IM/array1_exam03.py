arr = list(map(int, input().split()))
print('odd : {}'.format(sum(arr[::2])))
print('even : {}'.format(sum(arr[1::2])))