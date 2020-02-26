def prime_list(a, b):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (b+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int((b+1) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, b+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    if a == 1:
        return [i for i in range(a+1, b+1) if sieve[i] == True and str(D) in str(i)]
    else:
        return [i for i in range(a, b+1) if sieve[i] == True and str(D) in str(i)]

T = int(input())
for tc in range(T):
    D, A, B = map(int, input().split())
    
    print('#{} {}'.format(tc+1, len(prime_list(A, B))))