#Functions--------------->
# def calc_sum(a, z):
#     sum = a + z
#     print(sum)
#     return sum
# calc_sum(33, 34)
# calc_sum(34, 33)

# def Hello():
#     print("Hello")
# Hello()
# output = Hello()
# print(type(output))
# print(output) 

# def avg(a, b, c):
#     sum = a + b + c
#     Avg = sum / 3
#     print(Avg)
#     return Avg
# avg(98, 97, 95)

# print("Azaan", end=" ")
# print("Alwani")

# str = "AzaanAlwani"
# print(len(str))
# print(str)

# print(type(str))

#range()

# def calc_prod(a, z = 2):
#     prod = a * z
#     print(prod)
#     return prod
# calc_prod(6)

# def calc_prod(a=1, z=2):
#     prod = a * z
#     print(prod)
#     return prod
# calc_prod()

#Practice->
# cities = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"]
# def length(cities_list):
#     for city in cities_list:
#         print(len(city))

# print(length(cities))

# def print_city(cities):
#         for city in cities:
#             print(city, end=" ")
# print_city(cities)   

# def Factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)
#     return fact
# Factorial(3)        


# def currency(USD):
#     PKR = USD * 277.20
#     print("USD to PKR:", PKR)
# currency(90)

# num = int(input("Enter a number: "))
# def integers(num):
#     if(num % 2 == 0):
#         print("Even")
#     elif(num % 2 != 0):
#         print("Odd")    
# integers(num)

##Recursion-------------->
# def show(n):
#     if(n == 0):
#         return
#     print(n, end=" ")
#     show(n-1)
# show(5)    

# def factorial(n):
#     if(n == 1 or n==0):
#         return 1
#     return factorial(n - 1) * n
# print(factorial(4))

##Practice------------->
# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n - 1) + n
# print(sum(14))

# def pri(List, idx):
#      if(idx == len(List)):
#             return None
#      print(List[idx])
#      pri(List, idx + 1)
# List = ["a", "b", "c", "d", "e"]
# pri(List, 0)