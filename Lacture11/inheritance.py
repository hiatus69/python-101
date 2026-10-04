class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

class dog:
    species = 'mammal'

    def calAge(self, age):
        print('Dog age is: {}'.format(age*3))
        
class SomeBread(dog):
    pass

class SomeOtherBread(dog):
    species = 'canine'
    def calAge(self, age):
        print('Dog age is: {}'.format(age*4))

frank = SomeBread()
print(frank.species)  # Output: mammal
frank.calAge(5)  # Output: Dog age is: 15

bean = SomeOtherBread()
print(bean.species)  # Output: canine
bean.calAge(5)  # Output: Dog age is: 20