class Employee:
    company = "TechMahindra"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Madhur"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)