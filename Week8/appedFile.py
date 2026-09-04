# Using the 'with' statement to open a file and read its contents and close it automatically
with open("example.txt", "r")as file:
    content = file.read()
    print(content)
# no need to explicitly close the file, it will be closed automatically when the block is exited