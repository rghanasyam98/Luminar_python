#scope of variables

#global scope variable can be accessed anywhere
global_scope_variable=5

#local scope
#variable x and function fun2() have local scope cant access from outside of that scope
# def fun():
#     print("global scope variable in fun ",global_scope_variable)
#     x=10
#     print("fun",x)
#     def fun2():
#         print("global scope variable in fun2", global_scope_variable)
#
#         print("fun2",x)
#     fun2()
# fun()
# print(x)


# global keyword is used to set the scope of a local variable to global

def fun():
    print("global scope variable in fun ",global_scope_variable)
    global x
    x = 10

    print("fun",x)
    def fun2():
        print("global scope variable in fun2", global_scope_variable)

        print("fun2",x)
    fun2()
fun()

print("accessing a local scope variable outside of that scope",x)
