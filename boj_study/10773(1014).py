# 선언
numbers = []

# 입력
K = int(input())
for _ in range(K):
    num = int(input())
    # 장부 관리
    if num:
        numbers.append(num)
    elif numbers:
        numbers.pop()

# 출력
print(sum(numbers))