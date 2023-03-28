class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry, You Need Another ",self.needs," Rs. To Withdraw")
    def checkBalance(self):
        print("Current Balance : ",self.balance)

b1=Bank()
acno=int(input("Enter Account Number : "))
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial Balance : "))

b1.openAccount(acno,cname,balance)

while True:

    print("***************************************************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("***************************************************************")

    choice=int(input("Enter Your Choice : "))
    print("***************************************************************")

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("***************************************************************")
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("***************************************************************")
    elif choice==3:
        b1.checkBalance()
        print("***************************************************************")
    else:
        print("Good Bye, Thank You For Using Our Services")
        print("***************************************************************")
        break
