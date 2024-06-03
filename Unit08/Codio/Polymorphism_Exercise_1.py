import random  #  the random module is imported

class Lottery:
    def shuffle(self):
        """
        Generate a list of 5 random integers between 1 and 20.
        
        :return: list of 5 random integers
        """
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results

class PowerBall(Lottery):
    def shuffle(self):
        """
        Override the shuffle method to generate a list of 6 random integers between 1 and 99.
        
        :return: list of 6 random integers
        """
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results

# Testing the PowerBall class
powerball = PowerBall()
print(powerball.shuffle())  # Expected: list of 6 random integers between 1 and 99
