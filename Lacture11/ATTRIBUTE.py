class Dog:
    #Class attribute
    species = 'mammal'

    #initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

## Instantiate the Dog object
dog1 = Dog("Gohan", 3)
dog2 = Dog("Brownie", 5)

# Access the class attributes
print("{} is {} and {} is {}".format(dog1.name, dog1.species, dog2.name, dog2.species))

# Is Gohan a mammal?
if dog1.species == "mammal":
    print("{} is a {}".format(dog1.name, dog1.species))