class A:#SINGLE

    def triangle(self):
        for i in range(6,0,-1):
            print("*"*i)

class B(A):
    def fac(self):
          n = int(input("enter number"))
          fac = 1
          for i in range(1,n+1):
               fac=fac*i
               print(fac)

obj =B()
obj.triangle()
obj.fac()








                