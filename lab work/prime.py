# def prime (n):
#     prime = 0
#     for i in range (1,n+1):
#         if (n%i==0):
#           prime+=1
#     if prime==2:
#        print ("prime")
#     else:
#        print ("not prime")

# n = int(input("enter number"))
# prime(n)

def prime (n):
    prime=0
    for i in range(1,n+1):
        if (n%i==0):
            prime+=1
    if prime==2:
        return "prime"
    else:
        return "not prime"

n = int(input("enter number : "))
print (prime(n))            
