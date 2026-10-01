try:
    value = int(input('Enter a number: '))
    result = 10 / value
except ValueError:
    print('Please enter a number')
except ZeroDivisionError:
    print('cannot divide by zero')
else:
    print(result)
print('end of program')