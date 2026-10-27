import random
otp=random.randint(1001,9999)




d={}
while True :
    menu="""
    enter 1 for sign up :
    enter 2 for login :
    enter 3 for forgot password :
    enter 4 for exit:


   """
    print(menu)
    choice=int(input("enter your choice!!" ))

    if (choice==1):
        name=input("enter your name :")
        email=input("enter your email :")
        mobile=int(input("enter your mobile :"))
        password=input("enter your password :")
        cpassword=input("enter cpassword :")


        if password==cpassword:
            d['email']=email
            d['password']=password
            d['mobile']=mobile

            print("signup successfully!!")

        else:
            print("password and confirm password does not match!!")

    elif choice==2:
        email = input("enter your email :")
        password=input("enter your password :")

        if d['email']==email and d['password']==password:
            print("login successfully !!")
        else:
            print("invalid credentials!!")


    elif choice==3:
        mobile=int(input("enter mobile :")) 

        if d['mobile']==mobile:
            print("*****your otp is :",otp)

            uotp = int(input("enter your otp :  "))

            if otp==uotp:
                password = input("enter password : ")

                d['password']==password

                print("password updated: ")

            else:
                print("invalid otp !!")

        else:
            print("mobile number does not match !!")

    elif choice==4:
        print("thank you")
        break                              

        

   

    