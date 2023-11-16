# score=int(input("enter marks"))
# if score >=18:
#     print("passed")
# else:
#     print("failed")

# num=int(input("enter a number"))
# if num==0:
#     print("zero")
# elif num % 2 ==0:
#     print("even number")
# else:
#     print("odd")

# num=int(input("enter a number"))
# if num==0:
#     print("zero")
# elif num >0:
#     print("positive number")
# else:
#     print('negative number')

#nested if
num=int(input("enter a age"))
health=input("enter health")
if num >= 60:
    if health =="ok":
        print("you are eligible")
    else:
        print("health not ok")

else:
    print("not eligible")