try:
    value = int(input('Enter a number: '))
    result = 10 / value
except Exception as err:
    print(f"an error occurred: {err}")
else:
    print(result)
print('end of program')