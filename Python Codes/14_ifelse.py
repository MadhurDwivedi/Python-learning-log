# num = int(input("enter your number: "))
# if(num < 0):
#   print("Number is negative")
# elif (num == 0):
#   print("number is zero")
# elif (num == 999):
#   print("number is special")
# else:
#   print("number is positive")

# num = int(input("Enter your number: "))
# if (num < 0):
#   print("NUmber is negative")
# elif (num > 0):
#   if (num <= 10):
#     print("Number is between 1-10")
#   elif (num > 10 and num <= 20):
#     print("Number is between 11-20")
#   else:
#     print("Number is greater than 20")
# else:
#   print("Number is zero")

num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
num3 = float(input("enter your third number: "))

if (num1 > num2 and num1 > num3):
  print("num1 is greater")
elif (num2 > num1 and num2 > num3):
  print("num2 is greater")
else:
  print("num3 is greater")

if (num1 < num2 and num1 < num3):
  print("num1 is smallest")
elif (num2 < num1 and num2 < num3):
  print("num2 is smallest")
else:
  print("num3 is smallest")