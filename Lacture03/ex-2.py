employees_num= int(input("Enter number of employees: \n: "))

if employees_num < 50 and employees_num > 0:
    print("This is a small company.")
elif employees_num < 250 and employees_num > 0:
    print("This is a medium-sized company.")
elif employees_num >= 250:
    print("This is a large company.")