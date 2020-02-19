# 05_Homework

```python
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
```

> 1. 위와 같은 코드가 **fibo.py** 파일에 작성되어 있을 때, 아래와 같이 함수를 실행할 수 있도록 하는 import 구문을 (A), (B), (C)를 채워 넣어 완성하시오.

```python
from (A)fibo import (B)fibo_recursion as (C)recursion

recursion(4)
```



> 2. 다음 에러들이 어떠한 경우에 발생하는지 간단하게 작성하시오.

- ZeroDivisionError : 0으로 나눴을 경우
- NameError : 정의되지 않은 변수를 호출한 경우
- TypeError : 잘못된 자료형을 사용한 경우
- IndexError : 잘못된 Index를 사용한 경우
- KeyError : dictionary에 key가 없는 경우
- ModuleNotFoundError : 모듈을 찾을 수 없는 경우
- ImportError : 모듈은 찾았으나 가져오는 과정에서 실패하는 경우

