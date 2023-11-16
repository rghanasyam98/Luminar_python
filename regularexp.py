#regular expression
import re
# x="hello how are you"
#
# #match() : to check a particular sentance startswith a specific word
# print("case  of match ",re.match("hello",x))
# print("case of not match ",re.match("hai",x))
#
# #search(): to check a particular word exists or not in a sentance
# print("case  of searching match ",re.search("you",x))
# print("case  of  searching not match ",re.search("we",x))
#
# #rsub() to replace a word with another
# after_sub=re.sub("you","we",x)
# print(after_sub)

#to substitute decimal values
# z="my year of birth is 1999, 1999 is good year"
# after_removing_decimal=re.sub('\D'," ",z)
# print(after_removing_decimal)

# z="my year of birth is 1999, 1999 is good year"
# after_removing_decimal=re.sub('[0-9]',"*",z)
# print(after_removing_decimal)

#TO substitute small letter alphabets
# z="My year of birth is 1999, 1999 is good year"
# after_removing_decimal=re.sub('[a-z]',"*",z)
# print(after_removing_decimal)

# #TO substitute small and capital letter alphabets
# z="My year of birth is 1999, 1999 is good year"
# after_removing_decimal=re.sub('[a-z,A-Z]',"*",z)
# print(after_removing_decimal)

# # TO substitute all others excluding small letter alphabets
# z="My year of birth is 1999, 1999 is good year"
# after_removing_decimal=re.sub('[^a-z]',"*",z)
# print(after_removing_decimal)

# # TO substitute all others excluding small letter, capital letter alphabets,digits,space
# z="My year of birth is 1999, 1999 is good year @#$%"
# after_removing_decimal=re.sub('[^a-z,A-Z,\s,0-9]'," ",z)
# print(after_removing_decimal)

# #split
# # x="welcome to ootty nice to meat you"
# # y1=re.split("\s",x)
# # print(y1)
# #
# # #split by first space and to two
# # y2=re.split("\s",x,1)
# # print(y2)


# #findall
# x="hello hai how are you ,hello my name is hai"
# find_all=re.findall("hello",x)
# print(find_all)

# x='hello hello how are you hello +91989623457 yes sarangy1876@gmail.com helloo +91626989878 76868'
# y=re.findall("[0-9]",x)
# print(y)

x='hello hello how are fou hello fhjnashhd +9198962345 yes sarangy1876@gmail.com helloo +9162698987 76868'
# y=re.findall("[0-9]+",x)
# print(y)
#
# y2=re.findall("\w+",x)
# print(y2)

# y3=re.findall("[s]\w+[n]\w+[y]",x)
# print(y3)

#starts with a in bw n last d
# y4=re.findall("[a]\w+[n]\w+[d]",x)
# print(y4)

# #starts with f
# y4=re.findall("[f]\w+",x)
# print(y4)

#all 3 letter words
# y4=re.findall(r"\b\w{3}\b",x)
# print(y4)

#mobile numbers
# y4=re.findall(r"\b\d{10}\b",x)
# print(y4)

#matching email
# y4=re.findall("\w+[@][g][m][a][i][l][.][c][o][m]",x)
# print(y4)


#validity of password
#6-16 letters
#at least one a-z
#at least one A-Z
#at least one 0-9
#at least one [@#$%&*]

pin=input("Enter your password")
if re.match('^.{6,16}$', pin):
    if re.search(r'[a-z]',pin):
        # print("atleast one a-z")
        if re.search(r'[0-9]',pin):
            # print("have at least one digit")
            if re.search(r'[@#$%&]',pin):
                if re.search(r'[A-Z]', pin):
                    print("satisfied")
                else:
                    print("not have atleast one A-Z")

                # print("have special char")
            else:

                print("not have a special character")


        else:
            print("not have at least one digit")


    else:
        print("not  atleast one a-z")

else:
    print("must have a length between 6 and 16")





