"""
In the IDE to the left, the class Chef is already defined. Modify the compare method so that it uses operator overloading to compare 
two chefs and determine who has more Michelin stars. You can use either the > or < operators for your overloading.


class Chef:
  def __init__(self, name, cuisine, stars):
    self.name = name
    self.cuisine = cuisine
    self.michelin_stars = stars
    
  def compare(self, other_chef):
    pass
"""


class Chef:
    def __init__(self, name, cuisine, stars):
        """
        Initialize a Chef object with a name, cuisine, and Michelin stars.
        
        :param name: str, name of the chef
        :param cuisine: str, type of cuisine the chef specializes in
        :param stars: int, number of Michelin stars the chef has
        """
        self.name = name
        self.cuisine = cuisine
        self.michelin_stars = stars
    
    def __gt__(self, other_chef):
        """
        Overload the > operator to compare Michelin stars between two chefs.
        
        :param other_chef: Chef, another Chef object to compare with
        :return: bool, True if self has more Michelin stars than other_chef, False otherwise
        """
        return self.michelin_stars > other_chef.michelin_stars

    def compare(self, other_chef):
        """
        Compare Michelin stars between self and another Chef object and return the appropriate message.
        
        :param other_chef: Chef, another Chef object to compare with
        :return: str, message indicating who has more Michelin stars
        """
        if self > other_chef:
            return f'{self.name} has more Michelin stars than {other_chef.name}'
        else:
            return f'{other_chef.name} has more Michelin stars than {self.name}'

# Instantiate Chef objects
marco = Chef('Marco Pierre White', 'French, British', 3)
rene = Chef('Rene Redzepi', 'Nordic', 2)

# Test the compare method
print(marco.compare(rene))  # Expected: ‘Marco Pierre White has more Michelin stars than Rene Redzepi’
print(rene.compare(marco))  # Expected: ‘Marco Pierre White has more Michelin stars than Rene Redzepi’
