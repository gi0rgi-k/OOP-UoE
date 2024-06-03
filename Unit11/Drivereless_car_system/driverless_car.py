# The Sensor class ibelow is designed to simulate the input data from vehicle sensors, 
# specifically for detecting obstacles. It allows setting and retrieving information about obstacles, 
# including their type and proximity. 

class Sensor:
    """Simulates input data from vehicle sensors."""
    def __init__(self): # initializes an instance of the Sensor class
        self.obstacle_type = None # this attribute is initialized to None and is intended to store the type of 
                                  # obstacle detected by the sensor (e.g., "Pedestrian", "Car")
        self.proximity = None     # intended to store the proximity (distance) of the obstacle from the vehicle in meters.

    def set_obstacle(self, obstacle_type, proximity):
        """This method allows setting the obstacle type and proximity based on the input."""
        self.obstacle_type = obstacle_type
        self.proximity = proximity

    def get_obstacle(self):
        """Returns the set obstacle type and proximity."""
        return self.obstacle_type, self.proximity

# The Obstacle class represents an obstacle that has been detected by the vehicle's sensors. 
# This class is designed to store information about the type of obstacle and its distance from the vehicle, 
# and it provides a method to display this information.

class Obstacle:
    """Represents an obstacle detected by sensors."""
    def __init__(self, type, distance): # The constructor method initializes an instance of the Obstacle class 
                                        # where 'type' and 'distance' of the obstacle are stored as parameters.
        self.type = type
        self.distance = distance

    def __str__(self):
        return f"{self.type} at {self.distance} meters"

# The Map class in the provided code manages static geographical data using a dictionary to store predefined routes. 
# This class allows adding new routes and retrieving existing ones with their names.

class Map:
    """Manages static geographical data using a dictionary."""
    def __init__(self):

# 'routes' attribute is a dictionary that stores routes. Each key in the dictionary is a route name, and the corresponding value 
# is a list of waypoints (locations) that define the route.      

        self.routes = {
            'Default Route': ['Start', 'Interim Point', 'Default Destination']
        }

    def add_route(self, route_name, waypoints):
        """Adds a new route to the map."""
        self.routes[route_name] = waypoints

    def get_route(self, route_name):
        """Retrieves a route by name."""
        return self.routes.get(route_name)


# The Route class in the provided code is responsible for handling the planning and updating of paths based on the 
# routes defined in the Map class

class Route:
    """Handles the planning of paths."""
    def __init__(self, map_instance):
        self.map = map_instance
        self.current_route = self.map.get_route('Default Route') # This attribute stores the current route of the vehicle

    def update_route(self, route_name, manual_update=True):
        """Updates the route automatically (e.g. due to obstacle detection) or due to manual input."""
        if manual_update:
            self.current_route[-1] = route_name  # Update the destination manually 
                                                 # this is used when user overrides a new destination to autonomous vehicle.
        else:
            self.current_route[1] = route_name  # System automatic update (due to obstacle detection)
        print(f"Route updated to: {self.current_route}")

# The Navigator class in the provided code is responsible for managing the navigation of the driverless car. 
# It interacts with both the Map and Route classes to set and update the vehicle's path, as well as control the vehicle's speed.

class Navigator:
    """Manages navigation and interacts with the map and route."""
    def __init__(self, map, route):
        self.map = map
        self.route = route
        self.current_speed = 0  # Initialize speed to zero

    def set_speed(self, speed):
        """Sets the vehicle's speed to a new value specified by the user or autoamtically set by vehicle."""
        """current_speed is updated each time vehicle's speed changes"""
        self.current_speed = speed 
        print(f"Vehicle speed set to {self.current_speed} km/h.")

    def stop_car(self):
        """Stops the car."""
        print("Car has been stopped.")

    def select_route(self, route_name):
        """Allows selection of a route from the map."""
        self.route.update_route(route_name)

# The ObstacleDetector class in the provided code is responsible for detecting obstacles 
# using data from sensors and managing the vehicle's response to these obstacles. 
# It interacts with the Navigator, Sensor, and UserInterfaceCLI classes to handle obstacle detection and subsequent actions.
# Based on the type and proximity of the obstacle, it calls update_route (to change the direction), set_speed (to adjust the speed), 
# alert_user (to inform the user regarding the obstacles) and stop_car (to stop the car) methods from different classes.

class ObstacleDetector:
    """Detects obstacles using data from sensors."""
    def __init__(self, navigator, sensor, user_interface):
        self.navigator = navigator
        self.sensor = sensor
        self.user_interface = user_interface

    def detect_obstacle(self):
        obstacle_type, proximity = self.sensor.get_obstacle()
        self.user_interface.alert_user(f"Obstacle detected: {obstacle_type} at {proximity} meters")
        if proximity < 10:
            self.navigator.stop_car()
        elif 10 <= proximity <= 50:
            self.navigator.set_speed(20)
            self.navigator.route.update_route('Different Route', manual_update=False)
            self.user_interface.alert_user("Route has been adjusted due to obstacle detection.")

# The UserInterfaceCLI class in the provided code represents a command-line interface (CLI) for user interaction 
# with the driverless car system. It allows the user to select routes, start navigation, simulate obstacle detection, 
# stop the car, and exit the system.

class UserInterfaceCLI:
    """Interface for user interaction."""
    def __init__(self, navigator, obstacle_detector):
        self.navigator = navigator
        self.obstacle_detector = obstacle_detector

    def alert_user(self, message):
        """Alert the user with a specific message."""
        print(f"ALERT: {message}")

    def start(self):
        while True:
            print("\nDriverless Car System Menu")
            print("1. Select Route")
            print("2. Start Navigation")
            print("3. Simulate Obstacle Detection")
            print("4. Stop Car")
            print("5. Exit System")
            choice = input("Enter your choice: ")

            if choice == '1':
                route_name = input("Enter route name: ") # user can input the destination
                self.navigator.select_route(route_name)
                self.navigator.set_speed(60)  # Set default speed to 60 km/h after selecting a route
                print(f"Route {route_name} selected. Default speed set to 60 km/h.")
            elif choice == '2':
                print("Navigation Menu:")
                print("a. Display Current Route")
                print("b. Update Route")
                print("c. Set Speed")
                nav_choice = input("Choose an action: ")
                if nav_choice == 'a':
                    print(f"Current route: {self.navigator.route.current_route}")
                elif nav_choice == 'b':
                    new_route_name = input("Enter new route name: ")
                    self.navigator.select_route(new_route_name)
                elif nav_choice == 'c':
                    new_speed = int(input("Enter new speed for the car: "))
                    self.navigator.set_speed(new_speed)
            elif choice == '3':
                obstacle_type = input("Enter obstacle type (e.g., Pedestrian, Vehicle): ")
                proximity = int(input("Enter proximity of obstacle (in meters): "))
                self.obstacle_detector.sensor.set_obstacle(obstacle_type, proximity)
                self.obstacle_detector.detect_obstacle()
            elif choice == '4':
                self.navigator.stop_car()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")


# Execute the script directly.

if __name__ == "__main__":
    map_instance = Map()
    route_instance = Route(map_instance)
    navigator = Navigator(map_instance, route_instance)
    sensor = Sensor()
    ui = UserInterfaceCLI(navigator, None)  # Initially setting None for obstacle_detector
    obstacle_detector = ObstacleDetector(navigator, sensor, ui)
    ui.obstacle_detector = obstacle_detector  # Setting the obstacle_detector with the instance of UI
    ui.start()
