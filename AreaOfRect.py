class rectangle():
    def __init__(self,wid,le):
        self.width=wid
        self.length=le
    def area(self):
        return self.length*self.width
rectarea=rectangle(2,3)
print(rectarea.area())
