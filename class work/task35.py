# multilevel

class A:
    def triangle(self):
            for i in range(6,0):
                print("*"*i)
                
class B(A):
        def fac(self):
              n = int(input("enter number"))
              fac = 1
              for i in range(1,n+1):
                   fac=fac*i
                   print(fac)

class c(B):
      def pattern(self,n):
        for i in range(1,n+1):
             print(" "*(n-1)+"*"*(2-i*i))

obj =c()
obj.triangle                         
obj.fac
obj.pattern