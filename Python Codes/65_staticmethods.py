# def add(a, b):
#     return a + b
class Math:
    def __init__(self, num):
        self.num = num
    def addtonum(self, n):
        self.num  = self.num + n

    # ek class ke andar ek method banane ke liye self as a argument pass karna jaroori nahi hai
    @staticmethod
    def add(a, b):
        return a + b

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2))