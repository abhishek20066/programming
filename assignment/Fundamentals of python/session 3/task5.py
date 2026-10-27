num1 = float(input("enter your first number : "))
num2 = float(input("enter your second number : "))
operator = input ("enter operator(+,-,*,/): ")

if operator == "+" :
    print("result :",num1 + num2)
elif operator == "-":
    print("result :",num1 - num2)    
elif operator == "*" :
    print("result :", num1*num2)
elif operator == "/"  :
    print("result :", num1/ num2)
else:
    print("error : invalid operator")      
