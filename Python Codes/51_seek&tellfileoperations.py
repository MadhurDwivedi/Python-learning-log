with open('49_myfile.txt', 'r') as f:
    print(type(f))
    # this moves to the 10 byte in the file
    f.seek(10)

    # this is for reading the next 5 bytes
    data = f.read(5)
    print(data)