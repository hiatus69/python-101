class car:
    # Car class with attributes and methods
    wheels = 4

    def __init__(self,make,model,year):
        self.make = make # instance variable
        self.model = model # instance variable
        self.year = year # instance variable

    def start_enginge(self):
        return f"{self.make} {self.model} engine started."

    def stop_engine(self):
        return f"{self.make} {self.model} engine stopped."


#creating an object of the car class
my_car = car("Toyota", "Camry", 2020)

print(my_car.make) # Output: Toyota
print(my_car.model) # Output: Camry
print(my_car.year) # Output: 2020

print(my_car.start_enginge()) # Output: Toyota Camry engine started.
print(my_car.stop_engine()) # Output: Toyota Camry engine stopped.