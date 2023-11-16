# def display(name):
#     print(name)
# n=input("Enter name")
# display(n)

# def sum1(a,b):
#     sum=a+b;
#     return sum
# x=int(input("enter number1"))
# y=int(input("enter number2"))
# s=sum1(x,y)
# print(s)

#
# def product(a,b):
#     return a*b
# x=int(input("enter number1"))
# y=int(input("enter number2"))
# r=product(x,y)
# print(r)

#default argument

# def disp(a,b=5):
#     print(a,b)
# disp(10,15)
# disp(10)

# *takes the variable length argments as a tuple
# def fun(*num):
#     print(sum(num))
# fun(1,2,3,4)
# fun(1,2,3,4,5,6)

#method1
# def sum1(num):
#     sum=0
#     for i in range(1,num+1):
#         sum=sum+i
#     return sum
# limit= int(input("Enter limit"))
# print("sum is : ",sum1(limit))

# #method2
# def sum1(n):
#     return int(n*(n+1)*0.5)
# print("sum is : ",sum1(int(input("Enter limit"))))

# #method2
# # def sum1(n):
# #     return sum(range(n+1))
# # print("sum is : ",sum1(int(input("Enter limit"))))

# def fact(n):
#     if n<0:
#         print("negative number not allowd")
#         return
#     elif n==0:
#         print("factorial of 0 is 1")
#         return
#
#     else:
#         f = 1
#         while n >= 1:
#             f = f * n
#             n = n - 1
#         print("factirial is", f)
#
#
#
# l=int(input("Enter limit"))
# fact(l)

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     elif n<0:
#         return "not defined"
#     return n * fact(n - 1)
#
# print("factorial is ", fact(int(input("Enter number"))))
#
# add = lambda a,b: a + b
# sub = lambda a,b: a-b
# mul = lambda a,b: a*b
# div= lambda a,b: a/b
# while (1):
#
#     print("\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\nPress any other key to exit....")
#     ch = input("Enter any option: ")
#     if ch in ['1','2','3','4']:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         if ch == '1':
#             print(a, " + ", b, " = ", add(a, b))
#         elif ch == '2':
#             print(a, " - ", b, " = ", sub(a, b))
#         elif ch == '3':
#             print(a, " * ", b, " = ", mul(a, b))
#         elif ch == '4':
#             if b == 0:
#                 print("division by zero not allowed...")
#                 continue
#             print(a, " / ", b, " = ", div(a, b))
#
#
#
#     else:
#         print("EXITING...")
#         break


# exp=lambda n : n ** 2
# print(exp(int(input("enter number"))))

# exp=lambda a,b : a * b
# print("product is ",exp(int(input("enter first number")),int(input("Enter second number"))))

#
# rev=lambda s: s[::-1].upper()
#
# print(rev(input("enter string"))