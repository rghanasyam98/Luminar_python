import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

#type conversion

#int to float

x=50
print(float(x))

#int to complex

print(complex(x))

#float to complex
b=2.5
print(complex(b,5))

#float to int

y=10.5
print(int(y))

#float to string

print(str(y))
#string to integer
z="1"
print(int(z))

#conversion of a float string to integer
a="5.5"
print(int(float(a)))