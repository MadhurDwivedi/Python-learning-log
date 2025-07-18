# Public Access Modifier

# class Employee:
#     def __init__(self):
#         self.name = "Madhur"
# a = Employee()
# print(a.name)


# Private Access Modifier

# class Employee:
#     def __init__(self):
#         self.__name = "Madhur"
# a = Employee()
# # print(a.name) --> Cannot be accessed directly
# print(a._Employee__name) # -->Can be accessed directly


# Protected Access Modifier

class Student:
    def __init__(self):
        self._name = "Madhur"
    def _funName(self):
        return "CodeWithMadhur"

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())