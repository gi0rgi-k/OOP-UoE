"""Encapsulation Exercise 5"""

# Create Cyclist class
# The attributes _name, _nationality, and _nickname are protected 
# attributes following the Python convention (using a single underscore _).
class Cyclist:
# The __init__ method initializes the protected attributes 
# with the values passed as parameters.
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

# @property is used to define a getter method for each attribute.
# The getter methods (name, nationality, nickname) allow access to the protected attributes.
# The setter methods (name, nationality, nickname) allow modification of the protected attributes.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        self._nationality = nationality

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        self._nickname = nickname

# Initialize the Cyclist class object
my_cyclist = Cyclist("Greg LeMond", "American", "Le Monstre")

# Print the attributes
print(my_cyclist.name)          # Expected: Greg LeMond
print(my_cyclist.nationality)   # Expected: American
print(my_cyclist.nickname)      # Expected: Le Monstre

# Update the attributes
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"

# Print the updated attributes
print(my_cyclist.name)          # Expected: Eddy Merckx
print(my_cyclist.nationality)   # Expected: Belgian
print(my_cyclist.nickname)      # Expected: The Cannibal
