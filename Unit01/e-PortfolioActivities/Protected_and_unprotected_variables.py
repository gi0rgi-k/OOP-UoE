""""e-Portfolio Activity: Develop a Python program and apply protected and unprotected variables within it."""

"""
Below is an example of a Python program that demonstrates the use of protected and unprotected (public) variables. 
In Python, protected variables are indicated by a single underscore _ as prefix of the variable name,  
while public variables do not contain an underscore.
"""

#Example of a 'Car' class to demonstrate the difference of protected and unrotected variables in a class

class Car:
    def __init__(self, make, model, year, owner): #Initialise a car class
        self.make = make          # Public variable
        self.model = model        # Public variable
        self.year = year          # Public variable
        self._owner = owner       # Protected variable

    def display_info(self): #display/print method for each attribute in Car class
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Owner: {self._owner}")

    def modify_info(self, make, model, year, owner): #update/modification method for each attribute in car class
        self.make = make
        self.model = model
        self.year = year
        self._owner = owner

# Create an instance of the Car class
car = Car(make="Toyota", model="Corolla", year=2020, owner="George")

# Access and modify the variables
print("Before modification:")
car.display_info()

# Modify the public variables directly
car.make = "Honda"
car.model = "Civic"
car.year = 2022

# Modify the protected variable directly
car._owner = "Bob"

print("\nAfter modification directly:")
car.display_info()

# Modify using the class method
car.modify_info(make="Ford", model="Focus", year=2022, owner="Nick")

print("\nAfter modification using class method:")
car.display_info()
