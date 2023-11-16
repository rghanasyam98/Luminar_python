class bankaccount:
    def __init__(self, accno, name, typ, bal):
        self.accnum = accno
        self.nm = name
        self.ty = typ
        self.ba = bal

    def deposit(self, damnt):
        self.ba = self.ba + damnt
        print("SUCCESSFULLY DEPOSITED...,Your current balance is ", self.ba)

    def withdraw(self, wamnt):
        self.ba = self.ba - wamnt
        print("SUCCESSFULLY DEBITED...,Your current balance is ", self.ba)

    def balance(self):
        print("Current account balance : ",self.ba)


an = int(input("Enter account number: "))
na = input("Enter name: ")
t = input("Enter account type: ")
ba = int(input("Enter first deposit(min-500):"))
p1 = bankaccount(an, na, t, ba)

while (1):

    ch = int(input("If you want to withdraw press 1 ,deposite press 2 , 3 check balance ,unless any key..."))
    if ch == 1:
        wamount = int(input("Enter amount to debit.."))
        if p1.ba < wamount + 500:
            print("sorry You dont have enough balance to debit...")
        else:

            p1.withdraw(wamount)
    elif ch == 2:
        damount = int(input("Enter amount to deposite.."))
        p1.deposit(damount)

    elif ch == 3:
        p1.balance()
    else:
        print("Thank you come again...")
        break