class Airplane:
    def __init__(self, first_class, business_class, coach):
        """
        Initialize the Airplane class with the number of passengers in first class,
        business class, and coach class.

        :param first_class: int, number of passengers in first class
        :param business_class: int, number of passengers in business class
        :param coach: int, number of passengers in coach class
        """
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        """
        Calculate the total number of passengers on the airplane.

        :return: int, total number of passengers
        """
        return self.first_class + self.business_class + self.coach


class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        """
        Initialize the Train class with the number of passengers in each car.

        :param car1: int, number of passengers in car 1
        :param car2: int, number of passengers in car 2
        :param car3: int, number of passengers in car 3
        :param car4: int, number of passengers in car 4
        :param car5: int, number of passengers in car 5
        """
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        """
        Calculate the total number of passengers on the train.

        :return: int, total number of passengers
        """
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5


def passengers(obj):
    """
    Print the total number of passengers on board.

    :param obj: object, an instance of Airplane or Train class
    """
    print(f'There are {obj.total()} passengers on board.')


# Testing the code
airplane = Airplane(12, 24, 180)
train = Train(50, 60, 70, 80, 90)

passengers(airplane)  # Expected: There are 216 passengers on board.
passengers(train)     # Expected: There are 350 passengers on board.
