def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always executed")
# print("i am always executed")

x = func1()
print(x)