#enumerate
# to keep track of number of iterations of a loop
#while enumerating the value and iteration number returned as a tuple
lst1=[1,2,3,4,5]
obj=enumerate(lst1)
print(list(obj))

# string1="hello"
# obj2=enumerate(string1)
# print(list(obj2))
# print("first method")
# for i in enumerate(lst1):
#     print(i[0],":",i[1])
# print("second method")
# for i,j in enumerate(lst1):
#     print(i,":",j)


print("\n")

dict1={11:'raju',12:"ramu",13:"dolu",14:"bolu"}
for i,j in enumerate(dict1.keys()):
    print("loop count:",i,"key of dict:",j,"value of dict:",dict1[j])

print("\n")
for i,j in enumerate(dict1.values()):
    print("loop count:",i,"key of dict:",j)