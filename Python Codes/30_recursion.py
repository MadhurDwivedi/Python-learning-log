# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return (n * factorial(n-1))
    
# print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
series = [fibonacci (i)
          for i in range(5)]
print(series)
# print(fibonacci(4)) 