import sys
sys.stdin = open('부분집합의_합.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [num for num in range(1, 13)]
    count = 0
    
    for i in range(1<<len(arr)):
        sum_arr = []

        for j in range(len(arr)+1):
            if i & (1<<j):
                sum_arr.append(arr[j])
        if len(sum_arr) == N:
            result = 0
            for idx in range(N):
                result += sum_arr[idx]
            if result == K:
                count += 1
    print('#{} {}'.format(tc+1, count))
        
        
    
