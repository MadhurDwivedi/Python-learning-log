# str = "madhur"
# str = "mayank"
# print(str)

# list = ["madhur", 2, 2]
# list[0] = "mayank"
# print(list)
# print(id(list))
# list = list[1:]
# print(list)
# print(id(list)) 

# tup = ("madhur", 2)
# tup = ("mayank", 3)
# print(tup)
# set = {"madhur", 2, 2}
# set = {"mayank", 3, 3}
# print(set)
# dict = {
#     "name" : "madhur",
#     "age" : 2
# }
# print(dict)

tup = (1, 2, 3, 4, 76, 342, "green", True)
print(id(tup))
tup = tup[1:4]
print(tup)
print(id(tup))