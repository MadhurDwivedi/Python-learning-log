class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(Self):
        print("The default language is Python")

e1 = Employee("Madhur", 400)
e1.showDetails()
e2 = Programmer("Harry", 410)
e2.showDetails()
e2.showLanguage()