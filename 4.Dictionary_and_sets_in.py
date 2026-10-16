##Dictionary----------->
# dict = {
#     "key" : "value",
#     "name" : "Azaan Alwani",
#     "age" : 15,
#     "class" : 11,
#     "Learning" : "Python",
#     "grade" : "A*, B, A",
#     "subjects" : ["Maths", "English", "Accounts", "Economics", "BS Studies"],
#     "datatype" : ("Dictionary"),
# }
# print(dict)
# print(type(dict))
# print(dict["Learning"])
# dict["subjects"] = "Islamiat", "Urdu", "PST"
# print(dict["subjects"])
# dict["specs"] = True
# print(dict["specs"])
# print(dict)

#nested dictionary->

# nest_dict = {
#     "name" : "Mustafa",
#     "subjects" : {
#         "phys" : 67,
#         "maths" : 69,
#         "isl" : 100
#     }
# }
# print(nest_dict)
# print(nest_dict["subjects"]["phys"])

#Dictionary Methods->

# dict = {
#     "key" : "value",
#     "name" : "Azaan Alwani",
#     "age" : 15,
#     "class" : 11,
#     "Learning" : "Python",
#     "grade" : "A*, B, A",
#     "subjects" : ["Maths", "English", "Accounts", "Economics", "BS Studies"],
#     "datatype" : ("Dictionary"),
# }
# print(dict.keys())

# print(len(dict))

# print(dict.values())

# print(dict.items())

# print(dict.get("datatype"))

# dict.update({"city" : "Karachi"})
# print(dict)

##Sets---------------->
# collection = {1, 2, 2, 2, 3, 1.1, 6.6, "hey", 1, 4, 6.7, "hello", "world", "world"}
# print(collection)
# print(type(collection))
# print(len(collection))

# null_set = set()
# print(null_set)

#Set Methods->
# null_set = set()
# null_set.add(0)
# null_set.add("My")
# null_set.add("Name")
# null_set.add("is")
# null_set.add((6, 7))
# null_set.add([1, 2, 3]) #error
# print(null_set)

# null_set.remove("is")
# print(null_set)

# null_set.clear()
# print(null_set)
# print(len(null_set))

# set = {"Python", "is", "hello", "coding", "world"}
# print(set.pop())
# print(set)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.union(set2))

# print(set1.intersection(set2))

#Practice------------->
# wm = {
#     "table" : ["a piece of furniture, list of facts and figures"] ,
#     "cat" : "a small animal" 
# }
# print(type(wm))
# classrooms = {"Python", "Java", "Python", "C++", "C", "Java", "C++", "Python", "Javascript"}
# classes_required = len(classrooms)
# print(classes_required, "classes are required for all students")

# marks1 = int(input("Eco Marks : "))
# marks2 = int(input("BS Studies Marks : "))
# marks3 = int(input("Accounts Marks : "))
# dict = {}
# dict["Accounts"] = marks3
# dict["Economics"] = marks1
# dict["BS Studies"] = marks2
# print(dict)

# set = {9,'9.0'}
# print(set)
