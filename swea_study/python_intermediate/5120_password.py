T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = 0
    for _ in range(K):
        idx += M
        if idx >= len(arr):
            idx -= len(arr)
        arr.insert(idx, arr[idx-1]+arr[idx])
        print(idx, arr)
    # result = arr[-10:]
    # print('#{}'.format(tc), end=" ")
    # result.reverse()
    # print(*result)


# def crypto(pwd):
#     pivot = 0
#     start_num = pwd[pivot]

#     for _ in range(1, K + 1):
#         pivot += M

#         if pivot > len(pwd):
#             pivot -= len(pwd)

#         if pivot == len(pwd):
#             pwd.append(pwd[-1] + start_num)
#         else:
#             pwd.insert(pivot, pwd[pivot - 1] + pwd[pivot])
#         print(pivot, pwd)
#     return pwd


# T = int(input())

# for test_case in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     password = list(map(int, input().split()))

#     encrypted = list(reversed(crypto(password)))
    
#     # print(f'#{test_case}', end=' ')
#     # print(*encrypted[:10])