import random

print("what is my magic number (1 to 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber :
    msg = str(ntries) + " >> "
    if (ntries == 6):
        print("Your last chance: ")
    yourguess = int(input(msg))
    if yourguess > mynumber:
        print("Too high")
    elif yourguess < mynumber:
        print("Too low")
    ntries += 1
        
if yourguess == mynumber:
    print("Yes It is",mynumber)
else:
    print("No it not the number is: ", mynumber)