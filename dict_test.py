
dict={}
def add_data():
    name=input("Enter your name : ")
    if name in dict:
        print("Already exists...")
        return
    mob=input("Enter your phone : ")
    mail=input("Enter your mail : ")

    dict.update({name:{"name":name,"phone":mob,"mail":mail}})
    print("successfully added")

def view_data():
    name = input("Enter the name you want to search : ")
    if name in dict:
        print("Name : ",dict[name]["name"], " , Phone : ",dict[name]["phone"], " , Email : ",dict[name]["mail"])
    else:
        print("Not Found...")

def del_data():
    delkey = input("Enter the name you want to delete : ")
    if delkey in dict:
        del dict[delkey]
        print("successfully deleted")
    else:
        print("Not Found...")

def update_data():
    upkey = input("Enter the name you want to update : ")
    if upkey in dict:
        print("1.Name\n2.Mail\n3.Phone\n")
        backup_name=dict[upkey]["name"]
        backup_phone= dict[upkey]["phone"]
        backup_mail=dict[upkey]["mail"]
        choice=input("Enter the field you want to update...")
        if choice == "1":
            upname = input("Enter your name to update : ")
            del dict[upkey]

            dict.update({upname: {"name": upname, "phone": backup_phone, "mail": backup_mail}})
            print("successfully updated")

        elif choice == "2":
            upmail = input("Enter your mail to update : ")
            dict[upkey]["mail"]=upmail
            print("successfully updated")
        elif choice == "3":
            upmob = input("Enter your phone to update: ")
            dict[upkey]["phone"]=upmob
            print("successfully updated")
        else:
            print("invalid input..")
            return

    else:
        print("Not Found...")


while True:
    print("1.Add\n2.Update\n3.View\n4.Delete\nAny other key for exit\n")
    ch=input("Enter your choice : ")
    if ch=="1":
        add_data()
    elif ch =="2":
        update_data()
    elif ch =="3":
        view_data()
    elif ch =="4":
        del_data()
    else:
        print("Exiting...")
        break



# ddd={"name":"shyam","mob":123}
# print(ddd)
# ddd.update({"name":"tom"})
# print(ddd)
