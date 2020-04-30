N = int(input())
country = [list(map(int, input().split())) for _ in range(N)]
# border = [[] for _ in range(4)]
divide = []
people = 0

for d1 in range(N//2+1):
    for d2 in range(N//2+1):
        border = [[0]*N for _ in range(N)]
        for x in range(N-d1-d2):
            for y in range(d1, N-d2):
                
                divide.append(border)
                for i in range(N):
                    print(*border[i])
                print()
                
                



'''
6
1 2 3 4 1 3
7 8 9 1 4 2
2 3 4 1 1 3
6 6 6 6 9 4
9 1 9 1 9 5
1 1 1 1 9 9
'''