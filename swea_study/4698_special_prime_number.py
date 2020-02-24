def primeNum():
    for num in range(2, 10000):
        for n in range(2, 10000):
            if num == n:
                prime.append(num)
            if num % n == 0:
                break

T = int(input())
for tc in range(T):
    D, A, B = map(int, input().split())
    # prime = []
    # count = 0
    # if A % 2 == 0:
    #     for num in range(A+1, B+1, 2):
    #         for i in range(2, num+1):
    #             if num == i:
    #                 if divisor == 0 and str(D) in str(num):
    #                     count += 1
    #                 break
    #             if num % i == 0:
    #                 divisor += 1

    # for num in range(A, B+1):
    #     divisor = 0
    #     for i in range(2, num+1):
    #         if num == i:
    #             if divisor == 0 and str(D) in str(num):
    #                 count += 1
    #             break
    #         if num % i == 0:
    #             divisor += 1
    # # for n in prime:
    # #     if str(D) in str(n):
    # #         count += 1
    # print(count)
    # # print(len(prime))
    prime = []
    primeNum()
    print(prime)