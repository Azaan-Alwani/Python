##OOPS---------------->

#Classes = a reusable blueprint or template used to create objects.
#Objects = an instance of a class.

# class Student:
#     name = "Tom"
# s1 = Student()
# print(s1.name)    
# s2 = Student()
# print(s2.name)    

# class Factory:
#     color = "Black"
#     brand = "Pagani"# car1 = Factory()
# print(car1.color)
# print(car1.brand)

#__init__() = constructor method, executes when an object of the class is being initiated.

# class Student:
#      #default constructor
#     def __init__(self):
#         pass   
#     #parameterized constructor
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("addining new student in Database..")
# s1 = Student("Alice", 85)  
# print(s1.name, s1.marks)
# s2 = Student("Bob", 87)
# print(s2.name, s2.marks)

##Class and Instance Attributes-------------->

# class Student:
#     college_name = "Nixor College"  #class attribute
#     def __init__(self, fullname, marks):
#         self.name = fullname  #instance attribute
#         self.marks = marks    #instance attribute
#         print("adding new student in Database..")
# s1 = Student("Alice", 85)
# print(s1.name, s1.marks, s1.college_name)    
# # s2 = Student("Bob", 87) 
# # print(s2.name, s2.marks, s2.college_name)    
# print(s1.college_name)  #accessing class attribute using class name

# class Student:
#     college_name = "Nixor College"  #class attribute
#     name = "anonymous"  #class attr
#     def __init__(self, fullname):
#         self.name = fullname  #obj attr > class attr
#         print("adding new student in Database..")
# s1 = Student("Alice")
# print(s1.name, s1.college_name)        

#Class Methods->

# class Student:
#     college_name = "Nixor College"  #class attribute
#     name = "anonymous"  #class attr
#     def __init__(self, fullname):
#         self.name = fullname  #obj attr > class attr
#         print("adding new student in Database..")
#     def welcome(self):
#         print(f"Welcome {self.name} to {self.college_name}")
# s1 = Student("Alice")
# s1.welcome()
# s2 = Student("Tony")
# s2.welcome()

#Practice--------------->
# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#         print("adding new student in Database..")
#     def avg(self):
#         avg = (self.marks1 + self.marks2 + self.marks3) / 3
#         return avg
# s1 = Student("Alice", 85, 90, 95)
# print(s1.name, s1.marks1, s1.marks2, s1.marks3)        
# print(s1.avg())
# print(type(s1.avg()))

##Static decorator----------------->
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in Database..")
#     @staticmethod
#     def welcome():
#         print("Welcome to Nixor College")
# s1 = Student("Rock")
# print(s1.name)
# s1.welcome()            

##OOPS Pillars---------------->
#Abstraction = Hiding the implementation details and showing only the functionality to the user.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
#     def start(self):
#         self.acc = True
#         self.brake = False
#         self.clutch = False
#         print("Car is started")
# c1 = Car()        
# c1.start()

#Encapsulation = Wrapping up of data and functions into a single unit(class)

##Practice---------------->

# class Accounts:
#     Bank = "HBL"
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
#     @staticmethod
#     def debit(d):
#         print(f"Debiting amount: {d}")
#         return d
#     @staticmethod
#     def credit(c):
#         print(f"Crediting amount: {c}")
#         return c
# user1 = Accounts(1000, 456) 
# print(f"Initial balance of account number {user1.acc_no} is {user1.balance}")
# dr = user1.debit(1000)
# print(f"The balance of account number {user1.acc_no} is {user1.balance - dr}")
# bal = user1.balance - dr
# cr = user1.credit(990)
# print(f"The balance of account number {user1.acc_no} is {bal + cr}")

##delete keyword---------------->

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
# s1 = Student("Azaan")
# del s1
# print(s1.name)  #this will give error because s1 is deleted 


##Public Attributes and Methods-----------------> Accessible from anywhere, inside and 
#                                                outside the class.

##Private Attributes and Methods-----------------> Used only within the class and not
#                                                 accessible outside the class.

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass  #private attribute
#     def get_acc_pass(self):
#         print(f"Account password is: {self.__acc_pass}")  #private method
#     def __hello(self):
#         print("Hello, this is a private method.")
#     def  Hello(self):
#             self.__hello()  #private method can be called inside the class
# acc1 = Account(123, "abcde")
# print(acc1.acc_no)
# acc1.get_acc_pass() 
# print(acc1.Hello())      #accessing private method through public method
# print(acc1.__hello())  #this will give error because __hello() is private method

#Inheritance = The process of acquiring the properties and behaviors of a parent class 
#              into a child class.

# class Car:
#     color = "Burgundy"
#     @staticmethod
#     def start():
#         print("Car is started")
#     @staticmethod
#     def stop():
#         print("Car is stopped")
# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name
# car1 = Toyota("Corolla")
# car2 = Toyota("Camry")
# print(car1.name)
# car1.start()         
# print(car1.color)          

##Types of Inheritance----------------->
#Single Inheritance = A child class inherits from a single parent class.

# class Car:
#     color = "Burgundy"
#     @staticmethod
#     def start():
#         print("Car is started")
#     @staticmethod
#     def stop():
#         print("Car is stopped")
# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name
# car1 = Toyota("Corolla")
# car2 = Toyota("Camry")
# print(car1.name)
# car1.start()         
# print(car1.color)    

#Multi-level Inheritance = A child class inherits from a parent class, and then
#                          another child class inherits from that child class.

# class Car:
#     color = "Burgundy"
#     @staticmethod
#     def start():
#         print("Car is started")
#     @staticmethod
#     def stop():
#         print("Car is stopped")
# class BYD(Car):
#     def __init__(self, brand):
#         self.brand = brand
# class Shark(BYD):
#     def __init__(self, type):
#         self.type = type
# car1 = Shark("Hybrid")
# car1.start()
# car1.stop()
# print(car1.color)
# print(car1.type)

#Multiple Inheritance = A child class inherits from multiple parent classes.

# class School1:
#     school1 = "HPGS"
# class School2:
#     school2 = "City School"
# class Section(School1, School2):
#     def __init__(self, name):
#         self.name = name        
# secA = Section("A")
# print(secA.name)
# print(secA.school1)
# print(secA.school2)

##Super Method = A method used to call the parent class constructor from the child class.

# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car is started")
#     @staticmethod
#     def stop():
#         print("Car is stopped")
# class Toyota(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
# car1 = Toyota("Corolla", "Sedan")
# print(car1.name)
# car1.start()
# print(car1.type)
# car1.stop()

##Class decorator->

# class Person:
#     name = "Anonymous"
#     def change_name(self, name):
#         self.__class__.name = name
# p1 = Person()
# p1.change_name("Weekend")
# print(p1.name)
#OR->
# class Person:
#     name = "Anonymous"
#     @classmethod
#     def change_name(cls, name):
#         cls.name = name
# p1 = Person()
# p1.change_name("Weekend")
# print(p1.name)
#OR->
# class Person:
#     name = "Anonymous"
#     def change_name(self, name):
#         Person.name = name
# p1 = Person()
# p1.change_name("Weekend")
# print(Person.name)
# print(p1.name)

#Property Decorators->
# class Student:
#     def __init__(self, phy, chem, bio):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.bio) / 3) + "%"
# s1 = Student(85, 90, 95)
# print(s1.percentage)
# s1.bio = 60
# print(s1.percentage)        

##Polymorphism = Allows different types, classes, or functions to share the same 
#           name but exhibit different behaviors based on the context in which they
#           are used. 
#Operator Overloading = A form of polymorphism that allows operators to have 
#                       different behaviors based on the types of operands they
#                       are applied to. The behavior of that operator is decided 
#                       by the user.
#dunder functions = __function__ 

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def show_num(self):
#         print(f"{self.real} i + {self.img} j")
#     def __add__(self, num2):
#         new_real = self.real + num2.real
#         new_img = self.img + num2.img
#         return Complex(new_real, new_img)
#     def __sub__(self, num2):
#         new_real = self.real - num2.real
#         new_img = self.img - num2.img
#         return Complex(new_real, new_img) 
# c1 = Complex(5, 9)
# c1.show_num()
# c2 = Complex(3, 7)
# c2.show_num()
# c3 = c1 + c2
# c3.show_num()
# c4 = c1 - c2
# c4.show_num()

##Practice------------------->

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def Area(self):
#         self.area = 3.14 * (c1.radius * c1.radius)
#         return self.area
#     def Perimeter(self):
#         self.perimeter = 2 * 3.14 * c1.radius
#         return self.perimeter
# c1 = Circle(1)
# print(c1.radius)        
# print(c1.Area())
# print(c1.Perimeter())

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def show_details(self):
#         print("role = ", self.role)
#         print("dept = ",self.dept)
#         print("salary = ",self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", 5000000)    
# eng1 = Engineer("Azzuuu", 15)        
# eng1.show_details()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def greater(self, num2):
        if(self.price > num2.price):
            print("Order1 is greater than Order2")
        elif(num2.price > self.price):
            print("Order2 is greater than Order1")    
o1 = Order("Milk", 210)   
o2 = Order("Eggs", 180)
print(f"Item1 : {o1.item}, Price : {o1.price}")
print(f"Item2 : {o2.item}, Price : {o2.price}")
o1.greater(o2)