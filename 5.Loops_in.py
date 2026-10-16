##While Loop---------------->
# iterator = 1
# while iterator <= 5:
#     print("Hello")
#     iterator += 1

# i = 1
# while i <= 10:
#     print("apna college", i)
#     i += 1    

#Practice->
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
  
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# print("Table : ")    
# n = int(input("Enter your num : "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1 

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

#Break->

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# i = 0
# while i < len(nums):   
#     if(nums[i] == 49):
#         print("FOUND X at idx ", i)
#         break
#     else:
#         print("Finding...")
#     i += 1

#Continue->

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# i = 0
# while i < len(nums):   
#     if(nums[i] == x):
#         i += 1
#         continue
#     else:
#         print("Finding...")
#         i += 1

##For Loop------------>
# nums = [1, 2, 3, 4, 5, 6, 7]
# for val in nums:
#     print(val)

# str = "viralvelocity"
# for char in str:
#     print(char)
# else:
#     print("END")        

#Practice->

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for nums in list:
#     print(nums)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 9, 81, 100)
# x = 9
# el = 0
# for idx in tup:
#     if(idx == x):
#         print("X FOUNDED at index", el)
#     el += 1

##Range------------->
#(start?, stop, step?)->
# for i in range(10): #(stop)
#     print(i)

# for i in range(1, 8): #(start, stop)
#     print(i)

# for i in range(1, 10, 2): #(start, stop, step)
#     print(i)

#Practice->

# for i in range(1, 101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# table = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(i * table)

##Pass------------->
# for i in range(10):
#     pass

##Practice------------->
# n = int(input("Enter a natural number : "))
# i = 1
# sum = 0
# while i <= n:
#      sum += i
#      i += 1
# print(sum)

# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)    