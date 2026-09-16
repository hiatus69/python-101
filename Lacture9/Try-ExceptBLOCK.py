filename = input('Enter a filename: ')
try:
    #Open file.
    infile = open(filename, 'r')
    content = infile.read()
    print(content)
    infile.close
except IOError:
    print('An error occurred trying to read')
    print('the file', filename)
print("end of program")