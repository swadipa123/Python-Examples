# class Circle:
#     def testing(self):
#         print("this is testing")
# class Sphere(Circle):
#     def documenting(self):
#         print("this is A")
#     def testing(self):
#         print("this is A's testing")
    

# a=Circle()
# b=Sphere()
# a.testing()
# b.testing()



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


a=float(input("Enter radius: "))


obj=Circle(a)
obj1 = Sphere(a)

print("Area of Circle:",obj.area())
print("Area of Sphere:",obj1.area())

'''------output----
$ python inheritance_test_circle_sphere.py
Enter radius: 2.0
Area of Circle: 12.56
Area of Sphere: 100.48        '''