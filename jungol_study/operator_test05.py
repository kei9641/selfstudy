num1, num2 = map(int, input().split())
if num1 == num2:
    same = True
    difference = False
else:
    same = False
    difference  = True
print(int(same))
print(int(difference))