age = int(input("Please enter your age: "))
income = int(input("Please enter your income: "))

if age >= 18 and age<= 65 and income >= 50000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")