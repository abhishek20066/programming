#hierarchical inheritance
class A:
    def fun1(self):
        print("method 1")

class B(A):
    def fun2(self):
        print("method 2")

class C(A):
    def fun3(self):
        print("method 3")

obj1 = B()
obj1.fun1()
obj1.fun2()
obj2 = C()
obj2.fun1()
obj2.fun3()        
