class A:
    def prime(self):
        n=int(input("enter number :"))

        for i in range(1,n+1):
            if n%i==0:
                prime+=1
        if prime==2:
            print("prime")
        else:
            print("not prime")    

class B(A):
    def pattern(self,n):
        for i in range(1,n+1):
            print(" "*i)

class C(A):
    def evenodd(self):
        n=int(input("enter number :"))
        if n%2==0:
            print("even")
        else:
            print("odd")

class D(B,C):
    def tabel(self):
        n= int(input("enter number :"))
        for i in range(1,n+1):
            for j in range(1,11):
                print(f"{i}*{j}={i*j}")



obj = D()
obj.tabel()
obj.evenodd()
obj.pattern(5)
obj.prime()
