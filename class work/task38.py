import random
account_number =random.randint(10000000000,99999999999)

print("your account number :",account_number)
d={}

class Bank:
    def ac_open(self):
        name = input("enter your name :")
        mobile = input("enter your number :")
        password = input("enter your password")
        
        

        balance=5000
        self.balance=balance
    def deposit(self):
        damount=int(input("enter deposit number : "))
        if damount>30000:
            print("deposit ammount can not be more than 30000")



        else:
           self.balance+=damount

           print("deposit successfully!!")

    def withdraw(self):
        wamount=int(input("enter withraw number :"))

        if wamount>10000:
            print("withdraw ammount can not be more than 10000")
        else:    
          self.balance+-wamount
          print("withdraw successfully!!")

    def check_bal(self):
        print("your balance:",self.balance)
        if self.balance<0:
            print("self balance cannot be less than 0")
        
obj = Bank()

print("press 1 for account open")
print("press 2 for exit ")


choice= int(input("enter your choice : "))

if choice==1:

    obj.ac_open

    while True:
        menu=""""
        press 1 for deposit
        press 2 for withdraw
        press 3 for check balance
        press 4 for exit
        """
        print(menu)
        choice1=int(input("enter your choice"))

        if choice1==1:
            obj.deposit()
        elif choice1==2:
            obj.withdraw()

        elif choice1==3:
            obj.check_bal()

        elif choice1==4:
            break        




        
