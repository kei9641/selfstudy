def calculation(a, b, cal):
    if cal == '+':
        return a + b
    elif cal == '*':
        return a * b
    elif cal == '-':
        return a - b

N = int(input())
sentence = list(input())
#1, 2, 4, 7, 
# eval(), repr()