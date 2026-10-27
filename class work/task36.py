class A:
    def fun1(self):
        super().fun1()
           
        print("method 1")

class B():
    def fun1(self):
        print("method 2")
class C(A,B):
    def fun1(self):
        super().fun1()
        print("method 3")        

obj = C()
obj.fun1()

#multiple