"""Challenge"""

class Person:
    count = 0
    
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height, age=0, gender=''):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        self.this_age = age
        self.this_gender = gender
        self.bmi = ''
        Person.count += 1

    @classmethod
    def print_count(cls):
        return cls.count


class Adult(Person):
    """Represents an adult person."""
    def __init__(self, first, last, weight, height, age=0, gender=''):
        super().__init__(first, last, weight, height, age, gender)

    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)
        return bmi_tmp

    def get_bmi_classification(self):
        bmi_tmp = self.calc_bmi()
        if self.this_gender == 'M':
            return self.get_male_bmi(self.this_age, bmi_tmp)
        elif self.this_gender == 'F':
            return self.get_female_bmi(self.this_age, bmi_tmp)
        return 'Unknown'

    def get_male_bmi(self, age, bmi_temp):
        if bmi_temp < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi_temp < 24.9:
            return 'Normal'
        elif 25 <= bmi_temp < 29.9:
            return 'Overweight'
        else:
            return 'Obese'

    def get_female_bmi(self, age, bmi_temp):
        if bmi_temp < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi_temp < 24.9:
            return 'Normal'
        elif 25 <= bmi_temp < 29.9:
            return 'Overweight'
        else:
            return 'Obese'


class Teacher(Adult):
    """Represents a teacher with specific attributes for the type of education and BMI risk factor."""
    
    def __init__(self, first, last, weight, height, age, gender, teacher_type):
        super().__init__(first, last, weight, height, age, gender)
        self.teacher_type = teacher_type
        self.bmi_risk_factor = self.assign_bmi_risk_factor(teacher_type)
    
    def assign_bmi_risk_factor(self, teacher_type):
        if teacher_type == 'kindergarten':
            return 1
        elif teacher_type == 'secondary':
            return 2
        elif teacher_type == 'higher education':
            return 3
        else:
            return 0  # Unknown type

    def __str__(self):
        return ("Name: {} {}, Age: {}, Gender: {}, Weight: {} lbs, "
                "Height: {} inches, Teacher Type: {}, BMI Risk Factor: {}").format(
                self.first_name, self.last_name, self.this_age, self.this_gender, 
                self.weight_in_lbs, self.height_in_inches, self.teacher_type, 
                self.bmi_risk_factor)


# Example
a1 = Adult('George', 'Smith', 150, 62, 30, 'M')
t1 = Teacher('Mariam', 'Koridze', 140, 65, 35, 'F', 'higher education')

print(a1.first_name)
print(a1.calc_bmi())
print(a1.get_bmi_classification())

print(t1)
print(t1.calc_bmi())
print(t1.get_bmi_classification())
