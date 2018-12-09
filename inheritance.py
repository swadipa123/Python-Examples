class Param:
    def __init__(self, no1,no2):
        self.n1 = no1
        self.n2 = no2
class rectangle(Param):
    def __init__(self):
        Param.__init__(self)
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
 
print()