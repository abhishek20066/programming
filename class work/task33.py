class MyClass1:
    def factor(self):
        no = int(input("Enter A Number to get Factorial:"))
        fact=1
        for i in range(1,no+1):
            fact*=i
        print("The Factorial of ",no,"is :",fact)

class MyClass2:
    def pattern(self):
        for i in range(1,6):
            print(" "*(6-i),"*"*i)
        
class MyClass3:
    def prime(self): 
        no = int(input("Enter a Number To check if its Prime:"))
        count=0
        for i in range(no,0,-1):
            if(no%i==0):
                count+=1
        if(count==2):
            print("The Entered Number",no,"is a Prime Number:")
        else:
            print("The Entered Number",no,"is not a Prime Number")

class MyClass4:
    def table(self,n):
        for i in range(1,11):
           print(f"{i} x {n} = {i*n}")

while True:
    menu="""
    Enter 1 for Factorial:
    Enter 2 for pattern:
    Enter 3 for Prime Number:
    Enter 4 for Table:
    Enter 5 To Exit:
    """
    print(menu)
    choice = int(input("Enter Your Choice:"))
    if(choice == 1):
        obj = MyClass1()
        obj.factor()

    elif(choice == 2):
        obj = MyClass2()
        obj.pattern()

    elif(choice == 3):
        obj = MyClass3()
        obj.prime()   

    elif(choice == 4):
        obj = MyClass4()
        n1 = int(input("Enter a Number to print Table:"))
        obj.table(n1)

    elif(choice == 5):
        print("Thank You")
        break
    else:
        print("Invalid Output Please Run Again:")
        break