PI=3.14

class Circle():
    def __init__(self,radius):
        self.radius =radius
        
    def area(self):
        return PI*self.radius*self.radius
class Sphere(Circle):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 4*PI *self.radius**3    

class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
class cube(rectangle):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**3    

class square(cube):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**2  
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))

input_radius=float(input("Enter radius of circle and sphere: "))

obj=rectangle(a,b)
obj1 = cube(b)
obj2 = square(b)
print("Area of rectangle:",obj.area())
print("Area of cube:",obj1.area())
print("Area of square:",obj2.area())


obj_circle=Circle(input_radius)
obj_sphere = Sphere(input_radius)

print("Area of Circle:",obj_circle.area())
print("Area of Sphere:",obj_sphere.area())


'''-------output---------
$ python inheritance_test_hybrid.py
Enter length of rectangle: 2
Enter breadth of rectangle: 3
Enter radius of circle and sphere: 2.0
Area of rectangle: 6
Area of cube: 27
Area of square: 9
Area of Circle: 12.56
Area of Sphere: 100.48         '''