#filter
#filter(function,list)
# lst=[1,2,3,4,5,6,7,8]
# def even(num):
#     return num%2 == 0
# odd=lambda x: x%2 !=0
# print("even sublist : ",list(filter(even,lst)))
# print("odd sublist : ",list(filter(odd,lst)))


# list1=['a','c','d','a','b','a']
list2=['ramu','raju','dolu','bolu','rema','raju']

# def fun(x):
#    return x == 'a'
#
# print("a sublist : ", list(filter(fun, list1)))


# def fun(x):
#    return  'a' in x
# print("a sublist : ", list(filter(fun, list2)))

# def fun2(x):
#     return x.__contains__('a')
# print("a sublist : ", list(filter(fun2, list2)))

# list3=input("Enter coma separated names").split(",")
# print(list3)

#------------------------------------------------------------

#zip()
# #takes position matching elements from each list and returns as tuples
# print(list(zip([1,2,3,4,5,6],[10,11,12,33,55,67],[11,12,13,14,15,16])))
# # print(tuple(zip([1,2,3,4,5,5],[10,11,12,33,5,5],[11,12,13,14,5,5])))
# # print(set(zip([1,2,3,4,5,5],[10,11,12,33,5,5],[11,12,13,14,5,5])))
# #
# d1={'shyam':25,'tom':23}
# d2={'midun':22,'abi':23}
# print(list(zip(d1,d2)))
# print(dict(zip(d1,d2)))
#
# keylist=['a','b']
# value1=[1,2,3]
# value2=[4,5,6]
# print(dict(zip(keylist,[value1,value2])))


#map()

# sqlist=list(map(int,[1.0,2.0,3.0,4.0]))
# print(sqlist)

# sqlist=list(map(pow,[1,2,3,4],[2]*4))
# print(sqlist)

# numbers=[1,2,3,4]
# cubelist=list(map(lambda x : pow(x,3),numbers))
# print("cubelist",cubelist)

namelist=['ramu','raju','dolu']
lengthlist=list(map(lambda x:len(x),namelist))
print("length list",lengthlist)

namelist2=['ramu','ramu','dolu']
numlist1=[2,4,5,6,7]
numlist2=[2,4,5,6,7]

combinedlist=list(map(lambda x,y:(x+y),namelist,namelist2))
print("string list ",combinedlist)

sumlist=list(map(lambda x,y:(x+y),numlist1,numlist2))
print("sum list ",sumlist)