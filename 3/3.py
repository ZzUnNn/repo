import math
class Shape():
    def area(self):
        return 0
    def length(self):
        return 0
    def compare_area(self,another):
        if(self.area() > another.area()):
            return "larger"
        if(self.area() < another.area()):
            return "smaller"
        if(self.area() == another.area()):
            return "equal"
    def compare_length(self,another):
        if(self.length() > another.length()):
            return "larger"
        if(self.length() < another.length()):
            return "smaller"
        if(self.length() == another.length()):
            return "equal"
class square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*self.side
    def length(self):
        return self.side*4
class triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        p = (self.side1+self.side2+self.side3)/2
        return math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
    def length(self):
        return self.side1+self.side2+self.side3
class rectangle(Shape):
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2
    def area(self):
        return self.side1*self.side2
    def length(self):
        return 2*(self.side1+self.side2)
class circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def length(self):
        return 2*math.pi*self.r
    
Squre = square(3)
Triangle = triangle(3,3,3)
Rectangle = rectangle(3,4)
Circle = circle(3)
print(Shape.compare_area(Squre,Triangle))


    
        
