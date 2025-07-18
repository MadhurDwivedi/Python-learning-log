import os
folders = os.listdir("data")

print(os.getcwd())
os.chdir("/users")
print(os.getcwd())
# print(folders)

# for folder in folders:
#     # print(folder)]
#     print(os.listdir(f"data/{folder}"))