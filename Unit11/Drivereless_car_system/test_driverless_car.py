# test_driverless_car.py
# Import classes from the drivereless_car file to test the functions in those classes
from driverless_car import Map, Route, Navigator, Sensor, ObstacleDetector, UserInterfaceCLI

# Set up the necessary objects and their relationships to test the route selection functionality
def test_route_selection():
    map_instance = Map()
    route_instance = Route(map_instance)
    navigator = Navigator(map_instance, route_instance)

    # Test selecting a new route
    # Runnin "select_route('Berlin')" function should set "Berlin" as destination
    # therefore the Assert command is expected to return True for 'current_route' = '['Start', 'Interim Point', 'Berlin']'
    # since 'select_route' sets the destination (in this case to 'Berlin'), and 'Start' and 'Interim Point' remain unchanged in 
    # the Route dataset
    navigator.select_route('Berlin')
    assert navigator.route.current_route == ['Start', 'Interim Point', 'Berlin'], "Failed to select the new Route correctly."

# Set up the necessary objects and their relationships to test the obstacle detection functionality

def test_obstacle_detection():
    map_instance = Map()
    route_instance = Route(map_instance)
    navigator = Navigator(map_instance, route_instance)
    sensor = Sensor()

# A new class MockUI is used to simulate the UserInterfaceCLI class, but instead of printing messages, 
# it collects messages in a list, which are then later checked to verify that the correct 
# messages were generated during the test.
# Using MockUI class allows the test to verify that the correct messages are generated when obstacles are detected 
# without printing to the console. It makes it easy to check if the system behaves as expected by examining the contents of 
# mock_ui.messages (python, 2024).

    class MockUI:
        def __init__(self):
            self.messages = []
        def alert_user(self, message):
            self.messages.append(message)

# Creates an instance of MockUI, which will be used in place of the actual user interface.
    mock_ui = MockUI()

# Creates an instance of the ObstacleDetector class, passing the navigator, sensor, and mock_ui instances. 
# This allows the obstacle detector to use the mock user interface to retreive "alert" messages.

    obstacle_detector = ObstacleDetector(navigator, sensor, mock_ui)

    # Simulate obstacle detection within moderate proximity (10 - 50 meters) and test three functionalities:
    # 1) Setting the current_speed to 20 should update the speed of the vehicle to '20'
    # 2) After moderate proximity (10 - 50 meters) obstacle is set via 'sensor.set_obstacle', 'Routes' dataset should be updated 
    # with a new destination and the 'mock_ui' variable should store the alert:
    # "Route has been adjusted due to obstacle detection.", hence the second Assert statement should be true.
    # 3) Besides the speed, the Route (direction of the vehicle) should also get updated to 'Different Route'
    sensor.set_obstacle('Pedestrian', 30)
    obstacle_detector.detect_obstacle()
    assert navigator.current_speed == 20, "Failed to set speed correctly for moderate proximity."
    assert "Route has been adjusted due to obstacle detection." in mock_ui.messages, "Route adjustment alert failed to trigger."
    assert navigator.route.current_route[1] == 'Different Route', "Route was not updated to 'Different Route'."

# Below code runs the above defined functions.
# This script will execute the tests and print "All tests passed successfully!" if all assertions pass. 
# If any assertion fails, it will provide details on what went wrong.

if __name__ == "__main__":
    test_route_selection()
    test_obstacle_detection()
    print("All tests passed successfully!")
