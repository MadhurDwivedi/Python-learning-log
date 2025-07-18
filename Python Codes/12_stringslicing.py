name = "my name is madhur dwivedi"
name2 = "madhur"
# print(name[0:10])
# this includes 0 but not 10 which means only includes lower limit not upper limit.

# print(name[:10])
# they bove both will return same output because python takes 0 as default either you write or not.

print(name[1:10])
print(name[:])

print(name[0:-3])
print(name[:len(name) - 3])
# they both above will also give the same output because python takes len(name) as default either you write or not.

print(name[-1:-3])
# this will not give any output because python will take len(name) as default.
print(name[-3:-1])
# len(name) = 25 - 3 = 22(index) = e
# len(name) = 25 - 1 = 24(index) = i
# this includes 22 but not 24 which means e and d only

# this will give the output because python will take len(name) as default.

print(name[-4:-2])
# len(name) = 25 - 4 = 21(index) = v
# len(name) = 25 - 2 = 23(index) = e
# this includes 21 but not 23 which means v and e only

# for finding the length of the string
# len1 = len(name)
# print(len1)