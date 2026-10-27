age = int(input("enter your age : "))
time = int(input("enter current time (0-23): "))

if age >= 18:
    if time >=22 or time <=2:
        print("order allowed")
    else:
        print("order not allowed")
else:
    print("order not allowed ")            