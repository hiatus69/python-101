from functools import reduce

 # Using map to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# Using filter to extract numbers greater than 5
numbers = [1, 2, 3, 6, 7, 8, 10]
filtered_numbers = list(filter(lambda x: x > 5, numbers))
print(filtered_numbers) # Output: [6, 7, 8, 10]

# Using reduce to find the product of all numbers in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Output: 120