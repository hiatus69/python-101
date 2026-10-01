try:
    numerator= float(input('Enter the numerator: '))
    denominator= float(input('enter the denominator'))

    result = numerator / denominator
    print('the result is ',result)

except ZeroDivisionError:
    print("Error: you can't zero ")
except ValueError:
    print("Error: please enter number")
finally:
    print("finally Aizen is The best")
print('end')