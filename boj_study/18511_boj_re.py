N, K = input().split()
k = int(K)
set_K = list(input().split())
result = ''

if k == 1:
    for i in range(len(N)-1, -1, -1):
        if N[i] < set_K[0]:
            result += set_K[0] * (len(N)-(i+1))
            break
    else:
        result += set_K[0] * (len(N)-1)

while i < len(N):
    for j in range(len(set_K)-1, -1, -1):
        if N[i] == set_K[j]:
            result[i] = set_K[j]
            i += 1
            break
        elif N[i] > set_K[j]:
            result += set_K[j]
            i = len(N)
            break

print(result)