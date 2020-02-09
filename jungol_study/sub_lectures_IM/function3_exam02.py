def EvenOdd(num):
    if num > 2:
        EvenOdd(num-2)
    print(num, end=' ')

EvenOdd(int(input()))