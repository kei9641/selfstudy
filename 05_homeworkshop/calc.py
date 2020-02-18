def MySum(a, b):
    return a + b

def MySub(a, b):
    return a - b

def MyMul(a, b):
    return a * b

def MyDiv(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')