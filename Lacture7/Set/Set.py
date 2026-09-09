fruits = {'apple', 'banana', 'cherry'}

fruits.add('orange')  # Add a new fruits to the set
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits.remove('banana')  # Remove a fruits from the set
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

fruits.discard('grape')  # Discard a fruits that may not be in the set (no error)
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

removed_fruits = fruits.pop()
print(f"Removed fruits: {removed_fruits}")  # Output: Removed fruits: apple (or any other fruits)
print(fruits)  # Output: {'cherry', 'orange'} (remaining fruits in the set)

fruits.clear()  # Clear all fruits from the set
print(fruits)  # Output: set() (empty set)