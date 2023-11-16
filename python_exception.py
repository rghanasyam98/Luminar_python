#exception

#example for ZeroDivisionError
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# try:
#     print(n1 / n2)
# except ZeroDivisionError as e:
#     print("Zero division error: ",e)


#handling any exception
# try:
#     print(n1 / n2)
# except Exception as e:
#     print("Zero division error: ",e)


#example for TypeError
# n1=10
# n2="a"
# try:
#     print(n1 / n2)
# except (ValueError, ZeroDivisionError,TypeError ) as e:
#     print("Exception occured : ", e)


#example for ValueError
# try:
#     age = int(input("Enter your age: "))
#     print("Your age is:", age)
# except ValueError as e:
#     print("Invalid input:", e)


#index out of range
# lst=[1,2,3,4,5]
# try:
#     a=int(input("Enter the index"))
#     print(lst[a])
# except Exception as e:
#     print(e)


#raising exception explicitly
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))

# try:
#     if n2 == 0:
#         raise ZeroDivisionError("Invalid mathematical operation")
#     else:
#         print(n1/n2)
#
# except Exception as e:
#     print(e)

# try:
#     if n2 >n1 :
#         raise Exception("Operation Not Allowed")
#     else:
#         print(n1-n2)
#
# except Exception as e:
#     print(e)