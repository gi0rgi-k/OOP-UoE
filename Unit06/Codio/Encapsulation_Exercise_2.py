"""Encapsulation Exercise 2"""

# Define an Artist class
class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

# Initialize the Artist class object
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

# Print the attributes (expecting error messages)
try:
    print(my_artist.name)  # Should raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(my_artist.medium)  # Should raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(my_artist.style)  # Should raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(my_artist.famous_artwork)  # Should raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

# Accessing the attributes using name mangling
print(my_artist._Artist__name)           # Expected: Bill Watterson
print(my_artist._Artist__medium)         # Expected: ink and paper
print(my_artist._Artist__style)          # Expected: cartoons
print(my_artist._Artist__famous_artwork) # Expected: Calvin and Hobbes
