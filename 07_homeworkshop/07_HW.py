class Calculator:
    count = 0
    
    def info(self):
        print('나는 계산기 입니다.')
        
    @staticmethod
    def add(a, b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a + b} 입니다.')
        
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
        
c = Calculator()
c.info() # 나는 계산기 입니다.
Calculator.add(5, 3) # 5 + 3 는 8 입니다.
Calculator.add(10, 2) # 10 + 2 는 12 입니다.
Calculator.history() # 총 2번 계산 했습니다.