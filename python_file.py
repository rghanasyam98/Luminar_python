# #writing into a file
# f=open('document.txt','w')
# for i in range(1,11):
#     f.write(f"this is line {i}\n")
#
# f.close()
#
# #appending into a file
# f = open('document.txt', 'a')
# for i in range(1, 11):
#     f.write("this is appended line  %d\n"%i)
#     # f.write(f"this is appended line {i}\n")
#
#
# f.close()
#
# #reading a file
# with open('document.txt','r') as f1:
#     content=f1.read()
# print(content)
#
# #reading the first line only
# with open('document.txt','r') as f2:
#     line1=f2.readline()
# print(line1)

# to read specific number of characters only (10)
# with open('document.txt','r') as f3:
#     txt=f3.read(10)
#     print("first 10 characters: ", txt)
#     print("current file pointer position: ",f3.tell())
#     print("after read of 10 characters the pointer will starts from here : ",f3.readline())
#     f3.seek(0)
#     print("after seeking to start: ",f3.readline())
#     f3.seek(0, 2)
#     print("last line: ",f3.readline())
#     f3.seek(0)
#
#     print(f3.read(421))
#     print(f3.tell())
#
# with open('document.txt', 'r') as file:
#     line_count = 0
#     for line in file:
#         line_count += 1
#
# print("Total number of lines:", line_count)

#to remove a file

# import os
# print(os.path.exists("document.txt"))
#
#
# if os.path.exists("document2.txt"):
#     os.remove("document2.txt")
# else:
#     print("File not found...")



# try:
#     os.remove("document.txt")
# except Exception as e:
#     print(e)


#to copy data from one file to another
with open("hello.txt","r") as hello, open("hai.txt","w") as hai:
    hello_content = hello.read()
    hai.write(hello_content)

# hello=open("hello.txt","r")
# hai=open("hai.txt","w")
# hello.close()
# hai.close()


