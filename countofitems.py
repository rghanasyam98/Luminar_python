lst=[1,2,6,"a","s","a",2,2,1]
# lst=[]
dict={}
def dup_count(list1):
    for x in list1:
        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = 1

dup_count(lst)
print(dict)
