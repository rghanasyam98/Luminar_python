# Encapsulation
# ==================
# Encapsulation binds together the data and functions that manipulate the data,keeping it safe from interference and misuse.
# it describes the idea of wrapping data and the methods that work on data with one unit.
# this puts restrictions on accessing variables and methods directly and can prevent accidental modification of data.
# to prevent accidental change an object's variable can only be changed by an object's method.those types of variables
# known as private variables.(public,private,stronglyprivate)


# class Encapsulation:
#     def __init__(self,a,b,c):
#         self.public=a
#         self._protected=b
#         self.__private=c
# x=Encapsulation(11,4,5)
# x.public=200              #a,b yude value change cheyyam.but c pattilla it is private.
#
# print(x.public)
# x._protected=500
# print(x._protected)
# print(x.__private)             #suggetion varilla,error varum private aayaal,access cheyyan pattilla

# to prevent accidental change an object's variable can only be changed by an object's method

# class Encapsulation:
#     def __init__(self,a,b,c):
#         self.public=a
#         self._protected=b
#         self.__private=c
#
#     def printvalue(self):
#         print(self.__private)    #now private is accessible by methode
# x=Encapsulation(11,4,5)
# x.public=200
#
# print(x.public)
# x._protected=500
# print(x._protected)
# # print(x.__private)
# x.printvalue()


# class Encapsulation:
#     def __init__(self,a,b,c):
#         self.public=a
#         self._protected=b
#         self.__private=c
#
#     def printvalue(self):
#         print(self.__private)
#
#
# class Employee:
#     def __init__(self,a,b,c,d,e):
#         Encapsulation.__init__(self,a,b,c)
#         self.d=d
#         self.e=e
#
#     def hello(self):
#         print(self.public)
#         print(self._protected)
#         print(self.d)
#         print(self.e)
#
# x=Employee(11,4,5,3,7)
# x.hello()


# Super
# ====================

# it will make the child class inherit all the methods and properties from its parent

# class Encapsulation:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#
#     def printvalue(self):
#         print(self.c)
#
#
# class Employee(Encapsulation):
#     def __init__(self,a,b,c,d,e):
#         super().__init__(a,b,c)
#         self.d=d
#         self.e=e
#
#     def hello(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#         print(self.d)
#         print(self.e)
#
# x=Employee(11,4,5,3,7)
# x.hello()


 # class Encapsulation:
#     aaaaa=300          #static variable
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#
#     def printvalue(self):
#         print(self.c)
#
#
# class Employee(Encapsulation):
#     def __init__(self,a,b,c,d,e):
#         super().__init__(a,b,c)
#         self.d=d
#         self.e=e
#
#     def hello(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#         print(self.d)
#         print(self.e)
#
# x=Employee(11,4,5,3,7)                 #nonstatic
# x.hello()
#
# y=Employee(11,4,5,3,7)                #nonstatic
# y.hello()


# All objects share class or static variable.An instance or non_static variables are different for different objects
# static variables are allocated memory ones when the object for the class is created for the first time.
# static variables are created outside the methods and inside the class
# static variables can be accessed through a class but not directly with a instance.
# static variables behaviour doesnt change for every object.

# static function is used to acces static variables


class Encapsulation:
    pc=0          #static variable

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        Encapsulation.pc+=1

    def printvalue(self):

        print(self.b)


    def printvalue1(self):
        print("no.of persons=",Encapsulation.pc)


x=Encapsulation('saranya',4,5)                 #nonstatic
x.printvalue()