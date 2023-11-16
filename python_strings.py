str1="hello how are you,nice to  meet you"
print(str1[5])
print(str1[6])
print(str1[-1])
print(str1.upper())
print("count of space ",str1.count(' '))
print("position of you between 15 and 20 ",str1.find("you",15,20))
print("position of we ",str1.find("we"))
print("right position of you ",str1.rfind("you"))
lst=str1.split(" ")
print("after split",lst)
#joining list of strings in list
str2=" ".join(lst)
print(" after join ",str2)
print("After capitalization :  ",str1.capitalize())
print("After title method : ", str1.title())
print("To uppercase : ", str1.upper())
print("To lower : ", str1.lower())

print("upper or not a ", "a".isupper())
print("upper or not A ", "A".isupper())

print("lower or not a ", "a".isupper())
print("lower or not A ", "A".isupper())

print("digit or not 3 ", "3".isdigit())
print("aphabet or not 3 ", "3".isalpha())
print("aphanumeric or not @1a ", "@1a".isalnum())

print("startswith G ","Ghanasyam".startswith("G"))
print("endswith m ","Ghanasyam".endswith("m"))

print("welcome to ootty nice to meet you".startswith("nice",17))


