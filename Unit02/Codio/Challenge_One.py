"""
Challenge One
"""

class Person:
    count = 0

    """Represents a generic Person."""

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count += 1

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

    @classmethod
    def print_count(cls):
        return cls.count

    def print_self(self):
        bmi = self.calc_bmi()
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Weight (lbs): {self.weight_in_lbs}")
        print(f"Height (inches): {self.height_in_inches}")
        print(f"BMI: {bmi:.2f}")

    def weight_status(self):
        bmi = self.calc_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Good weight"
        else:
            return "Overweight"


# Sample data
p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

# Calculate and display BMI of each person
print(p.calc_bmi())
print(p2.calc_bmi())

# Print total count of Person objects
print(Person.count)
print(Person.print_count())

# Print self details
p.print_self()
p2.print_self()

# Show weight status
print(f"{p.first_name} is {p.weight_status()}")
print(f"{p2.first_name} is {p2.weight_status()}")
