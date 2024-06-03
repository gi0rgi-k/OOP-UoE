"""e-Portfolio Activity: Polymorphism"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Car(Vehicle):
    def __init__(self, make, model, year, autopilot=False):
        super().__init__(make, model, year)
        self.autopilot = autopilot

    def info(self):
        print(f"I am a car. Make: {self.make}, Model: {self.model}, Year: {self.year}, Autopilot: {self.autopilot}")

    def drive(self):
        if self.autopilot:
            print(f"The car {self.model} is driving autonomously.")
        else:
            print(f"The car {self.model} is being driven manually.")


class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def info(self):
        print(f"I am a truck. Make: {self.make}, Model: {self.model}, Year: {self.year}, Cargo Capacity: {self.cargo_capacity} tons")

    def drive(self):
        print(f"The truck {self.model} is transporting goods.")


class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def info(self):
        print(f"I am a bike. Make: {self.make}, Model: {self.model}, Year: {self.year}, Type: {self.bike_type}")

    def drive(self):
        print(f"The bike {self.model} is being ridden.")


# Sample data
car1 = Car("Tesla", "Model S", 2022, autopilot=True)
truck1 = Truck("Ford", "F-150", 2021, cargo_capacity=5)
bike1 = Bike("Yamaha", "YZF-R3", 2019, bike_type="Sport")

for vehicle in (car1, truck1, bike1):
    vehicle.drive()
    vehicle.info()
    vehicle.drive()
