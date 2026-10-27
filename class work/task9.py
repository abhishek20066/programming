i = 1 
ev=0
od=0
evsum=0
odsum=0
sum=0
while(i<=5):
    n = int(input("enter number :"))

    if(n%2==0):
      print("even")
      ev=ev+1
      evsum=evsum+n
    else:
        print("odd")
        od=od+1
        odsum=odsum+n
    sum=sum+n
    i=i+1

print("even count :",ev)
print("odd count:",od)
print(evsum)
print(odsum)
print(sum)