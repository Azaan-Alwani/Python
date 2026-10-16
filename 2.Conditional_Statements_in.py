##Strings---------->
# str1 = 'I am a string.'
# str2 = "Don't forget to include me."
# str3 = """You completely overlooked me."""

##Escape Sequence Charcters->
# str = "This is a string.\nIt is created in python"
# str1 = "This is a string.\tIt is created in python"
# print(str)
# print(str1)

##Basic Operations->
#Concatination and length = 
# str = "Azaan"
# str1 = "Alwani"
# final_String = str + " " + str1
# print(final_String)

# len = len(final_String)
# print(len)

##Indexing->
# str = "Python"
# print(str[0])

##Slicing->
# str = "Apna College"
# print(str[0:5])
# print(str[1:len(str)])
# print(str[:8]) # [0:8]
# print(str[6:]) # [6:13]

# str = "apple"
# print(str[-5:-2])

##Functions->
# str = "zatians_Coaching"
# print(str.endswith("g"))
# print(str.capitalize())
# print(str.replace("Coaching", "School"))
# print(str.find("C"))
# print(str.count("a"))

##Practice-------->
# Name = input("Enter your name : ")
# len = len(Name)
# print(len)

# Occurence = "Hi, I am a $tring in a double quote$ $tring"
# Count = Occurence.count("$")
# print(Count)

##Conditional Statements------->
# age = 22
# if(age>=19):
#     print("You are eligible for CNIC")

# light = "red"
# if(light == "green"):
#     print("Go!")
# elif(light == "red"):
#     print("Stop!")
# elif(light == "yellow"):
#     print("Start!")         
# print("end")

# light = "pink"
# if(light == "green"):
#     print("Go!")
# elif(light == "red"):
#     print("Stop!")
# elif(light == "yellow"):
#     print("Start!")         
# else:
#     print("Light is broken") 

##Nesting->
# age = 17
# if(age >= 18):
#     if(age <= 80):
#         print("You are eligible for driving")
# else:
#   print("You are not eligible for driving")      

##Practice---------->
# marks = int(input("Enter your marks : "))
# if(marks >= 90):
#     print("your grade is A")
# elif(marks >= 80 and marks < 90):
#     print("Your grade is B")
# elif(marks >= 70 and marks < 80):
#     print("Your grade is C")
# elif(marks >= 60 and marks <70):
#     print("Your grade is D")
# else:
#     print("You are failed!")   

# num = int(input("Enter a number : "))
# if(num % 2 == 1):
#     print("ODD")
# else:
#     print("EVEN")    

# numbera = int(input("Enter first number : "))
# numberb = int(input("Enter second number : "))
# numberc = int(input("Enter third number : "))
# if(numbera > numberb and numbera > numberc):
#     print(numbera ,"is the greatest of all time")
# elif(numberb > numbera and numberb > numberc):
#     print(numberb ,"is hte greatest of all time")
# elif(numberc > numbera and numberc > numberb):
#     print(numberc ,"is hte greatest of all time")      

num = int(input("Enter your number : "))
if(num % 7 == 0):
    print("It is a multiple of 7")
else:
    print("It is not a multiple of 7")    