dict={'name':'shyam','mob':8137097444}
print(dict)
print(dict['name'])
#accessing keys and values
print("keys",dict.keys())
print("values",dict.values())


# dict2={'names':['shyam','sharanya','tom'],'mail':['a','b','c'],'phone':[1,2,3],'course':['x','y','z']}
# print(dict2)
dict4={'shyam':['a',1,'x'],'tom':['b',2,'y'],'sharanya':[{'c',3,'z'}]}
dict3={'shyam':[{'email':'a','mob':1,'course':'x'}],'tom':[{'email':'b','mob':2,'course':'y'}],'sharanya':[{'email':'c','mob':3,'course':'z'}]}
print(dict3)
print(dict3['shyam'])
dict4['shyam']=['aaa',234,'sss']
print(dict4['shyam'])

dict4['shyam'][1]=123
print(dict4['shyam'])

dict4.update({'rema':['a',1,'x']})
print(dict4)

#accessing value using get()
print(dict4.get('tom'))
print(dict4.get('aswin','not found'))

#removing values from dictionary with del
del dict4['tom']
print(dict4)

#removing values from dictionary with pop
dict4.pop('rema')
print(dict4)
