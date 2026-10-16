##Types of Files--------------> All are stored in form of 0 and 1.
# Text Files->Data is stored in the form of text. It can be opened in any text editor.
#             The extension of text files is .txt, .docs, .log, etc.
# Binary Files->Data is stored in non-text format. It can be opened in a specific 
#               application. The extension of binary files is .jpg, .png, .mp3, .mp4, etc.

##Characters for File I/O
# r->Open a file for reading. (default)
# w->Open a file for writing. Creates a new file if it does not exist or truncates the
#    file if it exists.
# a->Open a file for appending data at the end of the file.
# x->Open a file for exclusive creation. If the file already exists, the operation fails.
# b->Open a file in binary mode.
# t->Open a file in text mode. (default)
# +->Open a file for updating (reading and writing).
# r+->Open a file for reading and writing. The file pointer is placed at the beginning
#    of the file. There is no truncation.
# w+->Open a file for reading and writing. There is truncation.
# a+->Open a file for reading and writing. The file pointer is at the end of the file. 
#     There is no truncation.

#Opening a File->
# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#Reading a File->
# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "r")
# data = f.read(8)
# print(data)

# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "r")
# Line1 = f.readline()
# print(Line1)

# Line2 = f.readline()
# print(Line2)

#Writing a File->
# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "w")
# f.write("Hello World!")
# f.close()

# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "a")
# f.write("\nHello World!")
# f.close()

#Note: If the file is not present in the specified location, then python will create a
#      new file with the given name and extension.

# f = open("Sample.txt", "w")
# f.close()

# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "r+")
# f.write("You are") #Overwriting in the beginning of the file.
# print(f.read())
# f.close()

# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "w+")
# print(f.read()) #File is truncated, so nothing will be printed.
# f.write("abc")
# f.close()

# f = open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "a+")
# f.write("abc")
# print(f.read()) 
# f.close()

##With Syntax------------------->
# with open("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "r") as f:
#     data = f.read()
#     print(data)
#     f.close() #This is not necessary as the file will be closed automatically.

# with open ("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\demo.txt", "w") as f:
#     f.write("Hello World!")

##Deleting a File------------------->
# import os
# os.remove("C:\\Users\\HP\\OneDrive\\Documents\\My Code\\Python\\sample.txt")

##Practice------------------->
# with open("Practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Python", "Java")
# print(new_data) 
# with open("Practice.txt", "w") as f:
#     f.write(new_data) 
# def find_word():
#     with open("Practice.txt", "r") as f:
#         data = f.read()
#         if(data.find("learning") != -1):
#             print("Found")
#         elif(data.find("learning") == -1):
#             print("Not Found")
# find_word()        

# with open("Practice.txt", "r") as f:
#     data = f.readlines()
# for line in data:
#     if line.find("learning") != -1:
#         print(1)
#         break   

# import os
# os.remove("Practice.txt")