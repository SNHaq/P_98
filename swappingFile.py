def swap():
    fileA = input("Please enter your first file here: ")
    fileB = input("Please enter your second file here: ")
    #data_a = open("fileA")
    #data_b = open("fileB")
    with open(fileA, 'r') as a:
        data_a = a.read()
    with open(fileB, 'r') as b:
        data_b = b.read()
    with open(fileA, 'w')as a:
        a.write(data_b)
    with open(fileB, 'w')as b:
        b.write(data_a)

swap()