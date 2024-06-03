class Median:
    def calculate_median(self, *args):
        """
        Calculate the median of the integers passed to the method.
        Accepts anywhere from two to five parameters.

        :param args: int, variable number of integer arguments (2 to 5)
        :return: float, median of the integers
        """
        if not 2 <= len(args) <= 5:
            raise ValueError("This method accepts between 2 to 5 integers.")
        
        # Convert args to a list and sort it
        numbers = sorted(args)
        
        # Calculate the median
        n = len(numbers)
        if n % 2 == 1:  # If odd, return the middle element
            median = numbers[n // 2]
        else:  # If even, return the average of the two middle elements
            median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
        
        return median

# Testing the Median class
m = Median()

# Testing with different sets of parameters
print(m.calculate_median(3, 5, 1, 4, 2))  # Expected: 3
print(m.calculate_median(8, 6, 4, 2))     # Expected: 5.0
print(m.calculate_median(9, 3, 7))        # Expected: 7
print(m.calculate_median(5, 2))           # Expected: 3.5
