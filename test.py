class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Child(Parent):
    def __init__(self, g, x, y):
        super().__init__(x, y)
        self.g = g



    def firstMethod(self):
        print(self.y + '\n' + self.x + '\n' + self.g)


Yy =  Child('gg', 'xx','yy')
Yy.firstMethod()