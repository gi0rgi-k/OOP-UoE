"""Tutorial Lab 1: Inherit from a Base Class"""

class Person:
    count = 0
    
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height, age, gender):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        self.this_age = age
        self.this_gender = gender
        self.bmi = ''
        Person.count = Person.count + 1

       @classmethod
       def print_count(cls):
                return cls.count

class Adult(Person):
    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / self.height_in_inches ** 2

        print('BMI number is: ' + str(bmi_tmp))
        
        if bmi_tmp < 18:
            self.bmi = 'Underweight'
        elif bmi_tmp > 18 and bmi_tmp < 25:
            self.bmi = 'Normal'
        elif bmi_tmp > 25 and bmi_tmp < 30:
            self.bmi = 'Overweight'
        elif bmi_tmp > 30:
            self.bmi = 'Obese'
        return self.bmi

a1 = Adult('Tom', 'Thumb', 150, 62, 45, 'M')

print(a1.first_name)
print(a1.this_age)
print(a1.calc_bmi())
