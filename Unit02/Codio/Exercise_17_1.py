"""Exercise 17.1"""

"""
Using Time2.py, change the attributes of Time to be a single integer representing seconds since midnight. 
Then modify the methods (and the function int_to_time) to work with the new implementation. 
You should not have to modify the test code in main. 
When you are done, the output should be the same as before.
"""


from __future__ import print_function, division


class Time:
    """Represents the time of day.
       
    attributes: seconds_since_midnight
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        self.seconds_since_midnight = hour * 3600 + minute * 60 + second

    def __str__(self):
        """Returns a string representation of the time."""
        hour, minute, second = int_to_time(self.seconds_since_midnight)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Returns the number of seconds since midnight."""
        return self.seconds_since_midnight

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return Time(0, 0, seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        return Time(0, 0, self.time_to_int() + seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return self.seconds_since_midnight >= 0


def int_to_time(seconds):
    """Returns hour, minute, second from seconds since midnight."""
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return hour, minute, second


def main():
    start = Time(9, 45, 0)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
