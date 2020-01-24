# 11022번

# 입력 횟수를 설정하는 변수 repeat
repeat = int(input())
# a, b 리스트 초기화
a = list()
b = list()
# 각 입력값을 임시 저장하는 리스트 num
num = list()

for i in range(repeat):
    # repeat만큼 반복하여 값 입력
    num.extend(input().split())

a.extend(num[::2]) # 짝수 인덱스 값만 저장
b.extend(num[1::2]) # 홀수 인덱스 값만 저장

for i in range(repeat):
    print('Case #{}: {} + {} = {}'.format(i + 1, a[i], b[i], int(a[i]) + int(b[i])))
