userBook = {}

while True:
    print("1. ADD\n2. UPDATE\n3. DELETE\n4. VIEW\n5. EXIT")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter your name: ")
        emailCount = int(input("Enter your number of emails: "))
        emailList = []
        for i in range(emailCount):
            em = input("Enter email: ")
            emailList.append(em)

        phoneCount = int(input("Enter your number of mobile numbers: "))
        phoneList = []
        for i in range(phoneCount):
            ph = input("Enter phone: ")
            phoneList.append(ph)

        userBook.update({name:{"Name": name, "email": emailList, "phone": phoneList}})
        print("User added successfully!")

    elif ch == 2:
        userName = input("Enter your name for updating")
        if userName in userBook:
            updateChoice=int(input("1.update email\n2.update phone"))
            if updateChoice==1:
                index=0
                for email in userBook[userName]["email"]:
                    index = index + 1
                    print(index,":",email)
                updateIndex=int(input("enter number you want to update"))
                newEmail=input("enter new email")
                userBook[userName]["email"][updateIndex-1]=newEmail
                print("email updated successfully!")

            elif updateChoice ==2:
                index = 0
                for phone in userBook[userName]["phone"]:
                    index = index + 1
                    print(index, ":", phone)
                updateIndex = int(input("enter number you want to update"))
                newPhone = input("enter new phone")
                userBook[userName]["phone"][updateIndex - 1] = newPhone
                print("phone updated successfully!")
            else:
                print("invalid choice ")
                break
        else:
            print("invalid user ")
            break



    elif ch == 3:
        userName = input("Enter your name for deletion operations")
        if userName in userBook:
            deleteChoice = int(input("1.delete email\n2.delete phone"))
            if deleteChoice == 1:
                index = 0
                for email in userBook[userName]["email"]:
                    index = index + 1
                    print(index, ":", email)
                deleteIndex = int(input("enter number you want to delete"))
                del userBook[userName]["email"][deleteIndex-1]
                print("email deleted successfully!")
            elif deleteChoice == 2:
                index = 0
                for phone in userBook[userName]["phone"]:
                    index = index + 1
                    print(index, ":", phone)
                deleteIndex = int(input("enter number you want to delete"))
                del userBook[userName]["phone"][deleteIndex-1]
                print("phone updated successfully!")
            else:
                print("invalid choice ")
                break
        else:
            print("invalid user ")
            break




    elif ch == 4:
        userName=input("Enter your name for displaying")
        print(userBook.get(userName,"user not found"))

    elif ch == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")

