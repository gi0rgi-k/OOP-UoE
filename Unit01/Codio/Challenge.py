class Person:
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

# Create five different Person objects with appropriate values
p1 = Person("Tom", "Keshelava", 180, 70)
p2 = Person("Fred", "Koridze", 200, 72)
p3 = Person("George", "Williams", 150, 68)
p4 = Person("Tanya", "Brown", 130, 65)
p5 = Person("Mary", "Jameson", 140, 64)

# Create a list to store the above Person objects
person_list = [p1, p2, p3, p4, p5]

# Use a 'for' loop to iterate over the list and print out the first names
for person in person_list:
    print(person.first_name)

