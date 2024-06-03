class Characters:
    def __init__(self, phrases):
        """
        Initialize the Characters class with a list of phrases.

        :param phrases: list of strings, phrases to be stored in the instance
        """
        self.phrases = phrases

    def total_characters(self):
        """
        Calculate the total number of characters in all phrases.

        :return: int, total number of characters in the phrases
        """
        return sum(len(phrase) for phrase in self.phrases)

    def __lt__(self, other):
        """
        Overload the < operator to compare based on the total number of characters.

        :param other: Characters, another instance of Characters to compare with
        :return: bool, True if the total number of characters in self is less than in other
        """
        return self.total_characters() < other.total_characters()

    def __gt__(self, other):
        """
        Overload the > operator to compare based on the total number of characters.

        :param other: Characters, another instance of Characters to compare with
        :return: bool, True if the total number of characters in self is greater than in other
        """
        return self.total_characters() > other.total_characters()

    def __eq__(self, other):
        """
        Overload the == operator to compare based on the total number of characters.

        :param other: Characters, another instance of Characters to compare with
        :return: bool, True if the total number of characters in self is equal to in other
        """
        return self.total_characters() == other.total_characters()

# Testing the code
sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)

# Comparing the instances
print(c1 > c2)  # Expected: True
print(c1 < c2)  # Expected: False
print(c1 == c1)  # Expected: True
