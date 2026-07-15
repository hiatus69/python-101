inchar = input("input one character: \n: ")
if inchar >= 'A' and inchar <= 'Z':
    print("This is an uppercase letter.", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("This is a lowercase letter.", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input Number.", inchar)
else:
    print("It is not a letter or a number.", inchar)