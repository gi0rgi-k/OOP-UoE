"""Tutorial Lab 2: Adding the Child Class"""

class Person:
    count = 0
    
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height, age = 0, gender = ''):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        self.this_age = age
        self.this_gender = gender
        self.bmi = ''
        Person.count = Person.count + 1

    @classmethod
    def print_count(cls,):
        return cls.count

class Child(Person):

    def get_male_bmi(self, age, bmi_temp):
        bmi_class = ''
        if self.this_age > 2 and self.this_age < 9:
            if bmi_temp < 14:
                bmi_class = 'Underweight'
            elif bmi_temp > 14 and bmi_temp < 17:
                bmi_class = 'Normal'
            elif bmi_temp > 17 and bmi_temp < 20:
                bmi_class = 'Overwight'
            else:
                bmi_class = 'Obese'
                      
        elif self.this_age > 9 and self.this_age < 16:
            if bmi_temp < 17:
                bmi_class = 'Underweight'
            elif bmi_temp > 17 and bmi_temp < 23:
                bmi_class = 'Normal'
            elif bmi_temp > 23 and bmi_temp < 25:
                bmi_class = 'Overwight'
            else:
                bmi_class = 'Obese'
                        
        elif self.this_age >= 16:
            if bmi_temp < 19:
                bmi_class = 'Underweight'
            elif bmi_temp > 19 and bmi_temp < 23:
                bmi_class = 'Normal'
            elif bmi_temp > 23 and bmi_temp < 25:
                bmi_class = 'Overwight'
            else:
                bmi_class = 'Obese'
        
        return bmi_class

    def get_female_bmi(age, bmi_temp):

        return 'Not implemented'
        
    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / self.height_in_inches ** 2
        if self.this_gender == 'M':
            self.bmi = self.get_male_bmi(self.this_age, bmi_tmp)
        elif self.this_gender == 'F':
            self.bmi = self.get_female_bmi(self.this_age, bmi_tmp)
        return self.bmi

a1 = Adult('Tom', 'Thumb', 150, 62)
c1 = Child('Mark', 'Smith', 98, 48, 15, 'M')

print(a1.first_name)
print(a1.calc_bmi())

print(c1.first_name)
print(c1.calc_bmi())
