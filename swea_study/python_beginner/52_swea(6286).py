# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 11

'''
리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

예제 출력)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55] 
'''
# solution 1

def fibonacci(num): 
    a, b = 0, 1
    for i in range(num): 
        a, b = b, a+b 
    return a

fibo = [fibonacci(i) for i in range(1, 11)]
print(fibo)


# solution 2

def fibonacci(num): 
    if num < 2: 
        return num 
    else: 
        return fibonacci(num-1)+fibonacci(num-2)

fibo = [fibonacci(i) for i in range(1, 11)]
print(fibo)