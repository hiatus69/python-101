with open("example.txt", "r")as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())