print("Addition")
a=10
b=5
c=a+b
print(c)

print("Subtraction")
print(a-b)
print("Product")
print(a*b)
print("Division")
print(a/b)
print("Exponential")
print(a**b)
print("Modulus")
print(a%6)

print("Assignment operators")
a+=1
print("+=",a)
a-=1
print("-=",a)
a*=10
print("*=",a)
a%=3
print("%=",a)

print("Type checking",type(a)==type(b))

a=10
print("comparison operators")
if(a==10):
    print("a is 10")
if(a>b):
    print("a>b")
if a>=10:
    print("a >= 10")

if a<=10:
    print("a <= 10")
if a != 5:
    print("a is not 5")

print("Logical operators")

b=10
if a==10 and b==10:
    print("a is 10 and b is 10")
b=5
if a==10 or b==10:
    print("a is 10 or b is 10")
print("NOT operator",not True)

print("Identity operators")
print("is:",a is 10)
print("is not:",a is not 10)

print("Membership operators ")

name="ghanasyam"
print("in:","a" in name)
print("not in:","a" not in name)