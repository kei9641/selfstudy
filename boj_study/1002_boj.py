# 1002번

import math

# 테스트 케이스의 개수
repeat = int(input())

# 조규현
x1 = list()
y1 = list()
r1 = list()

#백승환
x2 = list()
y2 = list()
r2 = list()

x_len = list()
d = list()

# 입력값 나누기
for i in range(repeat):
    numbers = input()
    num = list(map(float, numbers.split()))

x1.extend(num[::6])
y1.extend(num[1::6])
r1.extend(num[2::6])

x2.extend(num[3::6])
y2.extend(num[4::6])
r2.extend(num[5::6])

for i in range(repeat):
    # x_len = int(x2[i]) - int(x1[i])
    # y_len = int(y2[i]) - int(y1[i])
    x_len.extend(x2[i] - x1[i])
    print(x_len)
    # d = math.sqrt((x_len ** 2) + (y_len ** 2))



# for i in range(repeat):
#     x_len = float(x2[i]) - float(x1[i])
#     y_len = float(y2[i]) - float(y1[i])
#     d.extend(math.sqrt((x_len * x_len) + (y_len * y_len)))
# print(d)

# X_length = float(x2-x1)
# Y_length = float(y2-y1)
 
# Dpl = math.sqrt((X_length*X_length)+(Y_length*Y_length))

# if (r1-r2) > Dpl :
#     turtle.write("두번째 원이 첫번째 원의 내부에 있습니다.")
    
# elif (r1-r2) == Dpl or (r1+r2) == Dpl :
#     turtle.write("두번째 원이 첫번째 원과 겹칩니다.")
 
# elif (r1-r2) < Dpl and (r1+r2) > Dpl :
#     turtle.write("두번째 원과 첫번째 원이 두점에서 만납니다.")
 
# else : 
#     turtle.write("두번째 원이 첫번째 원과 겹치지 않습니다.")