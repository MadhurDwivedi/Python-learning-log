class Person:
    name = "Madhur"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = "Harshit"
# a.occupation = "Accountant"
a.info()