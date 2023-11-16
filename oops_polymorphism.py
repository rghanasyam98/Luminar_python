#polymorphism

#same function with different implementation
#overloading and overriding
#function overloading => class is having functions with same name but different number ttype sequence of arguments

# class Shape:
#     def area(self,a=None,b=None):
#         return a*b
#     def area(self,r):
#         return 3.14*r*r
# obj=Shape()
# obj.area(10,10)
# obj.area(10)
#python not supports function overloading the above code results error

#alternate method for doing concept
# class Shape:
#     def area(self,a,b=None):
#         if b!=None:
#             return a * b
#
#         return 3.14*a*a
#
#
# obj=Shape()
# print(obj.area(10,10))
# print(obj.area(10))


# alternate method for doing concept
# class Shape:
#     def area(self,*a):
#         if len(a)==2:
#             x,y=a
#             return x+y
#         x=a[0]
#         return x
#
# obj=Shape()
# print(obj.area(10,10))
# print(obj.area(10))


#operat
# or overloading
# class Point:
#     def __init__(self,a):
#         self.a=a
#         # self.b=b
#     def __add__(self, other):
#         return self.a - other.a
#
#
# obj1=Point(10)
# obj2=Point(5)
# print(obj1+obj2)

# class Concat:
#     def __init__(self,a):
#         self.a=a
#         # self.b=b
#     def __add__(self, other):
#         return f"{self.a} {other.a}"
# obj1=Concat("welcome")
# obj2=Concat("to ootty")
# print(obj1+obj2)

# class Point:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         self.x=self.a + other.a
#         self.y=self.b + other.b
#         return Point(self.x,self.y)
#
#     def __str__(self):
#         return f"{self.a},{self.b}"
#
# obj1=Point(10,10)
# obj2=Point(5,5)
# print(obj1+obj2)

#overriding in python
class A:
    def display(self):
        print("class A")

class B(A):
    def display(self):
        print("class B")

obj=B()
obj.display()#in this case child method will be called
super(B,obj).display()