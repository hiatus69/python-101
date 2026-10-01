class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"invalid input: {value} is a negaive numner")

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    else:
        print(f"{num} is a valid positive number.")

try:
    number = int(input('Enter a positive number: '))
    check_positive_number(number)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Error: Please Enter a valid number")
except Exception as err:
    print(err)
finally:
    print("Kyouka Suigetsu")