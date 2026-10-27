n = int(input("enter number :")) #3268
rev = 0
rem = 0
n1 = n
while(n!=0):
    rem = n%10 #3268%10= 326.8
    rev=rev*10+rem   #0+8=8
    n=n//10  #326 32 3
print(rev)    

if n1==rev:
    print("palindrome!!")
else:
    print("not palidrome!1")    







    