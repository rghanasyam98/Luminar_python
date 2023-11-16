# college=['raju',24,'ramu',38,'dolu',89,3000.00,4000.00,5000.00]
# # str1=[]
# # int1=[]
# # float1=[]
# # for x in college:
# #     if type(x)==int:
# #         int1.append(x)
# #     elif type(x)==float:
# #         float1.append(x)
# #     else:
# #         str1.append(x)
# #
# # print(str1)
# # print(int1)
# # print(float1)

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j," ",end="")
#     print("\n")


# for i in range(1,7):
#     for i in range(1,i+1):
#         print(i," ",end="")
#     print("\n")
#
# for i in range(1,7):
#     for j in range(i+1,1,-1):
#         print(j," ",end="")
#     print("\n")


# for i in range(1,7):
#     x=[]
#     for j in range(1,i+1):
#         x.append(j)
#         # print(j," ",end="")
#     x.reverse()
#     for k in x:
#         print(k,end=" ")
#
#
#     print("\n")

#
# for i in range(1,7):
#     for j in range(i,0,-1):
#         print(j," ",end="")
#     print("\n")
#

#
for i in range(1,7):
    if i==1:
        print((25 - i) * "  ", end=" ")
    else:
        print((24 - i) * "  ", end=" ")

    for k in range(1,i+1):
        print(k,end=" ")
    print(" ",end="")
    if i !=1:
        for j in range(i, 0, -1):
            print(j, end=" ")

    print("\n")


# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("\n")

# for i in range(6,0,-1):
#     for j in range(1,i,1):
#         print(j,end=" ")
#     print("\n")


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print("\n")
