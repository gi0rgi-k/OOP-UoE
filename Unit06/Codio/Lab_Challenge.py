"""Lab Challenge"""

#Create a Person class with below methods nad attributes

class Person: 
    def __init__(self, name, age, occupation): 
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self, occupation):
        self.__occupation = occupation

# Testing the Person class
my_person = Person("Citra Curie", 16, "student")
print(my_person.get_name())          # Expected: Citra Curie
my_person.set_name("Rowan Faraday")
print(my_person.get_name())          # Expected: Rowan Faraday

print(my_person.get_age())           # Expected: 16
my_person.set_age(18)
print(my_person.get_age())           # Expected: 18

print(my_person.get_occupation())    # Expected: student
my_person.set_occupation("plumber")
print(my_person.get_occupation())    # Expected: plumber
