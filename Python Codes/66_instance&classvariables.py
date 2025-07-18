class Employee:
    companyName = "TechMahindra"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Madhur")
emp1.raise_amount = 0.3
emp1.companyName = "TCS"
emp1.showDetails()
emp2 = Employee("Kushagra")
emp2.showDetails()