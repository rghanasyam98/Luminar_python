#list
print("List")
lst1=[1,2,3.5,"ghanasyam",[4,5,6],{'key':'value'},(1,2,3),True]
print(lst1)
print(type(lst1))
lst2=list([1,2,3])
print(lst2)
lst2.pop()
print(lst2)
print(lst2.count(1))
lst2.insert(5,2)
print(lst2)
print(lst1[-3:-1])
print(lst1[-4:6])
print(lst1[:8])
print(lst1[1:-1])


print("swapping")
lst1[0],lst1[6]=lst1[6],lst1[0]
print(lst1)

lst3=["ramu","raju","dolu","bolu","rema"]
print(lst3)
lst3[2],lst3[3],lst3[4],lst3[0]=lst3[0],lst3[2],lst3[3],lst3[4]
print(lst3)
lst3.__setitem__(1,"radha")
print(lst3)

print("list functions")

print("append")

lst3.append("raju")
print(lst3)

print("insert")

lst3.insert(1,"shyam")
print(lst3)

#to add multiple items at a time
lst3.extend(["appu","kichu"])
print(lst3)

#the added item will be a list
# lst3.append(["arjun","akshay"])
# print(lst3)

#to remove items
#pop
#pops last item
# lst3.pop()
# print(lst3)
# #pops  item at index specified
#
# lst3.pop(1)
# print(lst3)
#
# #remove method
# lst3.remove("appu")
# print(lst3)

# #delete method
# # del lst3[0]
# # print(lst3)

# #to delete all items
# lst3.clear()
# print(lst3)

# lst3.extend(["apple","pineapple","babana"])
# print(lst3)
print('***')
#count of particular item
lst3.append("shyam")
print("count",lst3.count("shyam"))

#to sort a list
lst4=[3,2,8,5,4,1,9]
print(lst4.sort(reverse=True))
lst4.sort()
print(lst4)
lst4.sort(reverse=True)
print(lst4)

#to reverse a list
lst4.reverse()
print(lst4)
lst4=lst4[::-1]
print(lst4)

#length of a list
print("length",len(lst4))
#sum of elements
print(sum(lst4))
#max elemnt in a list
print(max(lst4))
#min elemnt in a list
print(min(lst4))


