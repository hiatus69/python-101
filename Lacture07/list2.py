# append method
fruits = ["apple", "banana", "cherry"]
more_fruits = ["mango", "pineapple"]
for fruit in more_fruits:
    print(f"Adding {fruit} to the fruits list.")
    fruits.append(fruit)
print(f"Updated fruits list: {fruits}")
print("----------------------------------------")

#insert method
berries = ["raspberry", "blackberry"]
berries.insert(1, "strawberry")
berries.insert(2, "blueberry")
print(f"Updated berries list with berries: {berries}")
print("----------------------------------------")

#remove method
fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Updated fruits list without duplicates: {fruits_with_duplicates}")
print("----------------------------------------")

#pop method
grades=[85, 90, 78, 92, 88]
third_grade = grades.pop(2)
grades.append(third_grade)
print(f"Updated grades list with popped grade: {grades}")
print("----------------------------------------")

#index method
animals = ["cat","dog","rabbit","hamster","dog","parrot","dog"]
first_dog_index = animals.index("dog")
print(f"The first occurrence of 'dog' is at index: {first_dog_index}")
second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")
third_dog_index = animals.index("dog", second_dog_index + 1)
print(f"The third occurrence of 'dog' is at index: {third_dog_index}")
print("----------------------------------------")

#clear method
fruits_to_clear = ["apple", "banana", "cherry"]
nested_list = [[1, 2, 3], [4,5,6], [7,8,9],[fruits_to_clear]]
print(f"Original nested list: {nested_list}")
for sublist in nested_list:
    sublist.clear()
print(fruits_to_clear)
print(f"Updated nested list after clearing: {nested_list}")
print("----------------------------------------")

#sort method
numbers_to_sort = [5, 2, 9, 1, 5, 6.1,]
numbers_to_sort.sort()
str_to_sort = ["banana", "apple", "cherry", "date"]
str_to_sort.sort()
print(f"Sorted numbers list: {numbers_to_sort}")
print(f"Sorted strings list: {str_to_sort}")

#reverse method
numbers_to_reverse = [1, 2, 3, 4, 5]
numbers_to_reverse.reverse()
str_to_reverse = ["apple", "banana", "cherry"]
str_to_reverse.reverse()
print(f"Reversed numbers list: {numbers_to_reverse}")
print(f"Reversed strings list: {str_to_reverse}")