# strings are immutable
a = "my name is madhur dwivedi!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))

# replace method
print(a.replace("madhur", "kushagra"))
b = a.replace("madhur", "kushagra")
print(b)

print(b.replace("dwivedi", "agrawal"))
print(a.split(" "))

blogHeading = "introduction to my family"
print(blogHeading.capitalize())

c = "welcome to the bangalore city!!"
print(len(c))
print(len(c.center(50)))

# variables can be overwrite in the python

print(a.count("a"))
print(a.endswith("!"))
print(a.find("z"))
print(a.find("m"))
print(a.find("n"))
print(a.find("w"))
# print(a.index("md"))

d = "Mynameismadhurdwivedi"
print(d.isalnum())
print(d.isalpha())

print(a.islower())
print(a.isprintable())
print(a.isspace())

e = "My Name Is Madhur Dwivedi"
print(e.istitle())

print(a.swapcase())
print(a.title())