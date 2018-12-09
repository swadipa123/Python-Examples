class A:
    def test(self):
        print("this is A")
class B:
    def test(self):
        print("This is B")
    def testing(self):
        print("this is another in B")
class C:
    def sdf(self):
        print("this is C") 
class D(C):
    pass
    # def sdf(self):
    #     print("this is D")
class X(B,A,D):
    pass

x=X()
x.test()
x.testing()
x.sdf()                                  