"""Exercise 16.2"""


# 1) Use the datetime module to write a program that gets the current date and prints the day of the week.

import datetime

def print_current_day_of_week():
    today = datetime.date.today()
    print("Today's date:", today)
    print("Day of the week:", today.strftime("%A"))

print_current_day_of_week()

# 2) Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until 
# their next birthday.

import datetime

def calculate_age_and_time_to_next_birthday(birthday):
    today = datetime.date.today()
    birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)
    
    if birthday_this_year < today:
        birthday_next_year = datetime.date(today.year + 1, birthday.month, birthday.day)
    else:
        birthday_next_year = birthday_this_year
    
    age = today.year - birthday.year
    if today < birthday_this_year:
        age -= 1

    time_to_next_birthday = birthday_next_year - today
    days = time_to_next_birthday.days
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print("Age:", age)
    print("Days until next birthday:", days)
    print("Hours until next birthday:", hours)
    print("Minutes until next birthday:", minutes)
    print("Seconds until next birthday:", seconds)

# Sample values
birthday = datetime.date(1999, 5, 15)  # Example birthday
calculate_age_and_time_to_next_birthday(birthday)


# 3) For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. 
# Write a program that takes two birthdays and computes their Double Day.

import datetime

def compute_double_day(birthday1, birthday2):
    if birthday1 > birthday2:
        birthday1, birthday2 = birthday2, birthday1

    diff = birthday2 - birthday1
    double_day = birthday2 + diff

    print("Double Day:", double_day)

# Example
birthday1 = datetime.date(1990, 10, 17)  # First birthday
birthday2 = datetime.date(2000, 8, 25)  # Second birthday
compute_double_day(birthday1, birthday2)


# 4) For a little more challenge, write the more general version that computes the day when one person is  

import datetime

def compute_n_times_older_day(birthday1, birthday2, n):
    if birthday1 > birthday2:
        birthday1, birthday2 = birthday2, birthday1

    initial_diff = birthday2 - birthday1
    total_diff = initial_diff * (n / (n - 1))
    n_times_older_day = birthday1 + total_diff

    print("Day when one person is {} times older than the other: {}".format(n, n_times_older_day))

# Sample usage
birthday1 = datetime.date(1990, 7, 20)  # First birthday
birthday2 = datetime.date(2000, 9, 5)  # Second birthday
n = 2  # Twice the age example
compute_n_times_older_day(birthday1, birthday2, n)




