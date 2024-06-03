"""Encapsulation Exercise 4"""

# Create a Dancer class
class Dancer:
    def __init__(self, name, nationality, style):
        self._name = name
        self._nationality = nationality
        self._style = style

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
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        self._style = style

# Initialize the Dancer class object
my_dancer = Dancer("Savion Glover", "American", "tap")

# Print the attributes
print(my_dancer.name)          # Expected: Savion Glover
print(my_dancer.nationality)   # Expected: American
print(my_dancer.style)         # Expected: tap

# Update the attributes
my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'

# Print the updated attributes
print(my_dancer.name)          # Expected: Anna Pavlova
print(my_dancer.nationality)   # Expected: Russian
print(my_dancer.style)         # Expected: ballet
