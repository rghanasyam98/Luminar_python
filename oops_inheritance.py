#inheritance
#inherits methods and attributes of another class
#base class,parent class,super class
#child class,subclass,derived class
#code reusability

# class A:
#     def displayA(self,name):
#         self.name=name
#         print("Class A")
# class B(A):
#     def displayB(self):
#         print("Class B")
# obj=B()
# obj.displayA("shyam")
# print(obj.name)
# obj.displayB()

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("Name:",self.name)
#
# class Person2(Person):
#     def __init__(self,name,age):
#         Person.__init__(self,name)
#         self.age=age
#     def display2(self):
#         print("Name:",self.name,"Age:",self.age)
#
# p1=Person2("shyam",25)
# p1.display()
# p1.display2()



#multiple inheritance
#
# class A:
#     def displayA(self):
#
#         print("Class A")
# class B:
#     def displayB(self):
#         print("Class B")
# class C(A,B):
#     def displayC(self):
#         print("Class C")
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

#multilevel inheritance
# class A:
#     def displayA(self):
#
#         print("Class A")
# class B(A):
#     def displayB(self):
#         print("Class B")
# class C(B):
#     def displayC(self):
#         print("Class C")

# obj=C()
#
# obj.displayA()
# obj.displayB()
# obj.displayC()



class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age

class College(Person):
    def setcollege(self,college_name):
        self.college_name=college_name

class Department(College):
    def setdepartment(self,dep_name):
        self.dep_name=dep_name
    def display(self):
        print("Name:",self.name,"Age:",self.age,"College:",self.college_name,"Departmnet:",self.dep_name)



student=Department()
student.setperson("shyam",25)
student.setcollege("kmct")
student.setdepartment("mca")
student.display()






# class College:
#     def __init__(self,college_name):
#         self.college_name=college_name
#     def displayCollege(self):
#         print(f"College : {self.college_name}")
#
# class Department:
#     def __init__(self,dep_name):
#
#         self.dep_name=dep_name
#     def displayDepartment(self):
#         print(f"Department : {self.dep_name}")
#
# class Student(College,Department):
#     def __init__(self,college_name,dep_name,student_name):
#         College.__init__(self, college_name)
#         Department.__init__(self,dep_name)
#         self.student_name=student_name
#     def displayStudent(self):
#         super(Student,self).displayCollege()
#         super(Student,self).displayDepartment()
#
#         print(f"Student Name : {self.student_name}")
#
# student=Student("KMCT","MCA","GHANASYAM")
# student.displayStudent()


