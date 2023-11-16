age=int(input("Enter age: "))
health=input("Enter health condition(ok/not_ok/critical) ")
dose=input("Enter vaccination first dose details(yes/no)")
priority="no"
if age >=18 and age< 60:
    priority = input("do you have priority(yes/no)")



if age>=60:
    if health == "critical":
        print("cant take your vaccination")
    elif health == "not_ok":
        print("submit reference from doctor to take vaccination")
    else:
        if dose == "yes":
            print("eligible to take second dose")
        elif dose == "no":
            print("eligible for first dose")
        else:
            print("booster doses are not available currently")
elif age >=18:
    if health == "critical":
        print("cant take your vaccination")
    elif health == "not_ok":
        print("submit reference from doctor to take vaccination")
    else:
        if priority=="yes":
            if dose == "yes":
                print("eligible to take second dose")
            elif dose == "no":
                print("eligible for first dose")
            else:
                print("booster doses are not available currently")

        else:
            print("you are currenty not eligible for vaccination")

else:
    print("age below 18 are currently not eligible for vaccination")
