x = 10
print(x)

def my_function():
    global x
    x = 4
    y = 5
    print(y)
my_function()
print(x)