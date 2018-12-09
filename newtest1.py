class Student:
    def __init__(self,stud_id,stud_name,age):
        self.stud_id=stud_id
        self.stud_name=stud_name
        self.age=age

s1=Student(1,"Payal",20)        
s2=Student(2,"Aasha",22)

print(s1.stud_name)
print(s2.age)