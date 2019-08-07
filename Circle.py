    
class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 3.14*2*self.radius
c1=circle(6)
print(c1.area())
print(c1.perimeter())
