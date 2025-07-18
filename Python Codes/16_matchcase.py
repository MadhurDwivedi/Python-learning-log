x = int(input("enter your number: "))
match x:
  case 0:
    print("x is zero")
  case _ if (x > 10):
    print("x is greater than 10")
  case _ if (x < 10):
    print("x is less than 10")
  case _:
    print(x)