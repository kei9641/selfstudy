from calc import MySum
from calc import MySub
from calc import MyMul
from calc import MyDiv

num1 = int(input())
num2 = int(input())

print(MySum(num1, num2))
print(MySub(num1, num2))
print(MyMul(num1, num2))
result = MyDiv(num1, num2)
if result != None:
    print(result)
