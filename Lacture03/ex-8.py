#two variable same reference
a = [1,2,3]
b = a 

# two variable different reference but same content
c = [1,2,3]
d = [1,2,3]

#using thee 'is' operator to check if two variables reference the same object in memory
print(a is b)  # True, because b references the same list as a
print(a is c)  # False, because c is a different list with the same content
print(c is d)  # False, because d is a different list with the same content

#using the '==' operator to check if two variables have the same content
print(a == c)  # True, because a and c have the same content
print(a == d)  # True, because a and d have the same content