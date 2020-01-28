'''
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
'''

three_num = list(map(int, input().split()))
three_num.pop(three_num.index(max(three_num)))
print(max(three_num))
