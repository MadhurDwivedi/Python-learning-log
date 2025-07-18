# def product(a = 7, b = 5, c = 2):
#     product = (a * b * c)
#     print("the product is: ", product)

# product()

def product(*numbers):
    product = 1
    for i in numbers:
        product = product * i
    # print("Product is: ", product)
    return product

a = product(5, 6)
b = product(7, 8)
print("the product we get in a is: ", a, "\nthe product we get in b is: ", b)

# def sum(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Product is: ", sum)

# sum(5, 6)