from abc import ABC,abstractmethod

#implementation details are given in child class method
# class A(ABC):
#     @abstractmethod
#     def fun1(self):
#         pass
#     def fun2(self):
#         print("class A fun2")
#
# class B(A):
#     def fun1(self):
#         print("abstract method implemented")
#     def fun3(self):
#         print("class B fun3")
#
#
# obj=B()
# obj.fun1()
# obj.fun2()
# obj.fun3()
#
# #cant create object for abstract class
# obj2=A()
# # obj2.fun1()
# obj2.fun2()




#obj=Hello1() without passing value solve error
# class Hello():
#     def __init__(self,name=None):
#         pass
#
# class Hello1(Hello):
#     def printa(self):
#         print("hai")
#
# obj=Hello1()
# obj.printa()


# class Hello:
#     def __init__(self, name):
#         pass
#
# class Hello1(Hello):
#     def __init__(self):
#         pass
#
# obj=Hello1()
