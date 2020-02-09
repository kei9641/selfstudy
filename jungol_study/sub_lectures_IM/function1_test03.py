n = int(input())
for i in range(1, n**2+1):
    print(i, end=' ')
    if i % n == 0:
        print()    
