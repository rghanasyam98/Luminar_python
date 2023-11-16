#range(start,end,step)
x=range(1,10,2)
print(x)
print(type(x))
#for loop
# for i in x:
#     print(i," ",end="")
# print("\nfirst loop over")
# for j in range(30,20,-5):
#     print(j," ",end="")
# print("\nsecond loop over")

#
# # x=[3,4,5,6,7]
# sum=0
# for i in [3,4,5,6,7]:
#     sum=sum+i
# print("sum is ",sum)

#method1
# odd=[]
# even=[]
# num1=[]
# for i in range(1,1000):
#     if i%2 !=0:
#         odd.append(i)
#     else:
#         even.append(i)
#     num1.append(i)
# print(odd)
# print(even)
# print(num1)
# #method 2
# odd1=[]
# even1=[]
# num2=[]
# for j in range(1,1000,2):
#     odd1.append(j)
#     even1.append(j+1)
#     num2.extend([j,j+1])
#
# print(odd1)
# print(even1)
# print(num2)

# pos,neg,z=[],[],[]
#
# for k in range(-100,100):
#     if k<0:
#         neg.append(k)
#     elif k==0:
#         z.append(k)
#     else:
#         pos.append(k)

# print(pos)
# print(neg)
# print(z)

pos,neg,z=[],[],[0]
for k in range(-100,0,1):
    neg.append(k)
    pos.append(abs(k))


print(pos)
print(neg)
print(z)