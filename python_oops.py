#class is defined by using class keyword
#convensionally class name starts with capital letter
#functions inside class known as methods

# class Person:
#     #self represents instance of class
#     #can access attributes and methods with self
#     #any name can use instead of self but advisable to use self for better readability
#     def read(self):
#         print("person is read")
#     def walk(self):
#         print("person is walking")
#
# p1=Person()
# p1.read()
# p1.walk()


# class House:
#     def person(self,name,color,floor,mob):
#         self.name=name
#         self.color=color
#         self.floor=floor
#         self.mob=mob
#     def display(self):
#         print("Name:",self.name,
#               "\nPhone",self.mob,
#               "\nColor:",self.color,
#               "\nFloor:",self.floor)
#
# obj1=House()
# obj1.person("shyam","yellow","marble","1111")
# obj1.display()
# print(obj1.name)


#constructor
#special method inside a class used for initialization at the time of object creation
# class House:
#     def __init__(self,name,color,floor,mob):
#         self.name=name
#         self.color=color
#         self.floor=floor
#         self.mob=mob
#     def display(self):
#         print("Name:",self.name,
#               "\nPhone",self.mob,
#               "\nColor:",self.color,
#               "\nFloor:",self.floor)
#
# obj1=House("ghanashyam","yellow","marble","1111")
# obj1.display()
# print(obj1.name)


# class House:
#     def __init__(self,name,color,floor,mob):
#         self.name=name
#         self.color=color
#         self.floor=floor
#         self.mob=mob
#     def display(self):
#         print("Name:",self.name,
#               "\nPhone",self.mob,
#               "\nColor:",self.color,
#               "\nFloor:",self.floor)
#
#
# n=int(input("Enter total number of houses"))
# # obj=
# lst=[]
# for i in range(n):
#     name=input("Enter name : ")
#     color=input("Enter color : ")
#     floor=input("Enter floor : ")
#     mob=input("Enter phone : ")
#     obj=House(name,color,floor,mob)
#     lst.append(obj)
#
# for x in lst:
#     x.display()
#
# obj1=House("ghanashyam","yellow","marble","1111")
# obj1.display()
# print(obj1.name)



# class House:
#     def __init__(self,name,color,floor,mob):
#         self.name=name
#         self.color=color
#         self.floor=floor
#         self.mob=mob
#     def display(self):
#         print("Name:",self.name,
#               "\nPhone",self.mob,
#               "\nColor:",self.color,
#               "\nFloor:",self.floor)
#
#
# n=int(input("Enter total number of houses"))
# # obj=
# lst=[None] * n
# for i in range(n):
#     name=input("Enter name : ")
#     color=input("Enter color : ")
#     floor=input("Enter floor : ")
#     mob=input("Enter phone : ")
#     lst[i]=House(name,color,floor,mob)
#
# for x in lst:
#     x.display()


#define a book class with the following attributes
#title author price
#defie a constructor to initialize the attributes of the method with values entered by the user
#set the view method to display information for the current book


#
# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def display(self):
#         print("Title:",self.title,
#               "\nAuthor",self.author,
#               "\nPrice:",self.price,)
#
# n=int(input("Enter total number of books"))
#
# lst=[None] * n
# for i in range(n):
#     title=input("Enter title : ")
#     author=input("Enter author : ")
#     price=int(input("Enter price : "))
#     lst[i]=Book(title,author,price)
#
# key=input("enter the title you want to search")
# flag=0
# for x in lst:
#     if x.title == key:
#         flag=1
#         print("title:",x.title)
#         print("Author:",x.author)
#         print("price:",x.price)
#     # x.display()
#
# if flag==0:
#     print("not found...")
#************************

#define a class which has atleast 2 methods
#one to get a string from console input and other is to print the string in uppercase

#
class StringExample:
    def getname(self):
        self.name=input("Enter name : ")
    def display(self):
        print(self.name.upper())

n=int(input("Enter total number of names"))
lst1=[None] * n
for i in range(n):
    lst1[i] =StringExample()
    lst1[i].getname()
for i in lst1:
    i.display()



