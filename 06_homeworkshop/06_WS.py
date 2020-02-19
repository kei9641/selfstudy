class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)

c = Circle(3, 2, 4)
print('원의 넓이: {0:.2f}'.format(c.area())) # 28.26
print('원의 둘레:{0:.2f}'.format(c.circumference())) # 18.84
