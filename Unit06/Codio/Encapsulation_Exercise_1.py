"""Encapsulation Exercise 1"""


# Create the country class with relevant private attributes, 
# and methods to display each attribute

class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

    def get_name(self):
        return self._name

    def get_capital(self):
        return self._capital

    def get_population(self):
        return self._population

    def get_continent(self):
        return self._continent


# Initialize the country class object
my_country = Country('France', 'Paris', 67081000, 'Europe')

# Print the attributes
print(my_country.get_name())        # Expected: France
print(my_country.get_capital())     # Expected: Paris
print(my_country.get_population())  # Expected: 67081000
print(my_country.get_continent())   # Expected: Europe


