N = int(input())
for x in range(N):
    for y in range(N):
        print('({}, {})'.format(x+1, y+1),end=' ')
    print()