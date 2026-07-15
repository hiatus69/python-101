operation = int(input("Please select an operation \n1 for addition \n2 for subtraction \n3 for multiplication \n4 for division \n: "))
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

if operation == 1:
    result = num1 + num2
    print("The result of addition is: ", result)
elif operation == 2:
    result = num1 - num2
    print("The result of subtraction is: ", result)
elif operation == 3:
    result = num1 * num2
    print("The result of multiplication is: ", result)
elif operation == 4:
    if num2 != 0:
        result = num1 / num2
        print("The result of division is: ", result)
    else:
        print("Error: Division by zero is not allowed.")