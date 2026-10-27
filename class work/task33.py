class MyClass:

    def prime(self):
            n = int(input("enter number :"))
            prime=0
            for i in range(1,n+1):
                if(n%i==0):
                    prime+=1
            if prime==2:
                print("prime")
            else:
                print("not prime")

class MyClass1:

     def triangle(self,n):
          for i in range(1,n+1):
               print("*"*i)
class MyClass2:

     def fac(self):
          n = int(input("enter number"))
          fac = 1
          for i in range(1,n+1):
               fac=fac*i
          print("factorial =",fac)     
class MyClass3:

     def evenodd(self):
          n= int(input("enter number :"))
          if(n%2==0):
               print("even")
          else:
               print("odd")

while True:
    menu= """
    enter 1 for prime:
    enter 2 for triangle:
    enter 3 for fac:
    enter 4 for evenodd:
    enter 5 for exit:

    """
    print(menu)
    choice = int(input("enter your choice  : "))

    if choice==1:
        obj = MyClass()
        obj.prime()

    elif choice==2:
         obj = MyClass1()
         obj.triangle(5)
    elif choice==3:
         obj = MyClass2()
         obj.fac()
    elif choice==4:
         obj=MyClass3()
         obj.evenodd() 

    elif choice==5:
        print("thank you")
        break
    else:
        print("invalid output please run again ")
        break                            


      
         
          
     


    
          






