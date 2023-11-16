# #
def validate_pin(pin):
    c=0
    for i in pin:
        c=c+1
    # print("length",c)
    if c not in [4,6]:
        return False

    for j in pin:
        if j not in ['1','3','5','7','9']:
            return False
    return True

password=input("Enter your pin")

result=validate_pin(password)
# print(result)
if result==True:
    print("password verified")
else:
    print("password authentication failed, invalid password")
#


# #
# def duplicte_count(lst1):
#     if type(lst1) != list:
#         return "invalid"
#     for x in lst1:
#         if x not in dict:
#             dict[x]=1
#         else:
#             dict[x]=dict[x]+1
#
# lst=[1,2,1,'a','b','b','b','1','1',5]
# # lst=[]
# # lst=(1,2,34)
# # lst={1,2,3,45}
# # lst="bcded"
# dict={}
#
# result=duplicte_count(lst)
# if result != "invalid":
#     print(lst)
#     print(dict)
# else :
#     print("invalid input")



# def validate_pin(pin):
#     c=0
#     for i in pin:
#         c=c+1
#     # print("length",c)
#     if c not in [4,6]:
#         return False
#
#     for j in pin:
#         if j not in ['1','3','5','7','9','0','2','4','6','8']:
#             return False
#     if int(pin)%2 == 0:
#         return False
#
#     return True
#
# password=input("Enter your pin")
#
# result=validate_pin(password)
# # print(result)
# if result==True:
#     print("password verified")
# else:
#     print("password authentication failed, invalid password")