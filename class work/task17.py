def add(a,b):
    sum = a+b
    return sum

def pattern():
    for i in range(1,5):
        print(" " *(5-i) , " *"*i)


def fac():
    n = int(input("enter number ;"))
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    return fac
def table(n):
    for i in range(1,11):
        print(f"{i} * {n} = {i*n}")

while True:
    menu="""
    enter 1 for add:
    enter 2 for pattern:
    enter 3 for factorial:
    enter 4 for table:
    enter 5 for exit:
    """             
    print(menu)
    choice = int(input("enter your choice"))
    if(choice ==1):
        a = int(input("enter number 1:"))
        b = int(input("enter number 2 :"))
        print(add(a,b))
    elif(choice==2):
        pattern()

    elif(choice==3):
        print(fac())

    elif(choice==4):
        tab = int(input("enter number :"))
        table(tab)
    elif(choice==5):
        print("thank you")
        break
    else:
        print("invalid output")
        break       


        
            




                   
