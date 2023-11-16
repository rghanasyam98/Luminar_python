s1={"shyam","sharanya","tom","tom"}
print(s1)

s2=set([1,2,3,2,1,4,5,"numbers"])
print(s2)

#add members to set
s1.add("aswin")
print(s1)

# #removes any random element
# print("before pop",s1)
# s1.pop()
# print("after 1st pop",s1)
# s1.pop()
# print("after second pop",s1)



#remove particular element
s1.remove("tom")
print(s1)

#set union method 1
set1={1,2,3}
set2={2,3,4,5}
set3=set1.union(set2)
print("union",set3)

#set union method 2

set4={1,2,3}
set5={2,3,4,5}
set6=set.union(set4,set5)
print("union",set6)

#intersection
intr=set1.intersection(set2)
print("intersection",intr)

intr2=set.intersection(set1,set2)
print("intersection",intr2)

#set differenc
diff=set.difference(set2,set1)
print("difference",diff)

print("%%%",set1.difference(set2))

# #to clear all values
# diff.clear()
# print(diff)

#to check 2 sets are disjoint or not

print("disjoint status ",set1.isdisjoint(set2))