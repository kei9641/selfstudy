'''
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
https://www.acmicpc.net/problem/1003
'''

def fibonacci(N):
    global fibo_0, fibo_1
    a, b = 1, 0

    for _ in range(N):
        a, b = b, a + b
    fibo_0, fibo_1 = a, b
    return fibo_1

T = int(input())
for tc in range(T):
    N = int(input())
    fibonacci(N)
    print('{} {}'.format(fibo_0, fibo_1))

# 함수 안에 global 변수를 사용해서 return없이 호출 가능!!!!
