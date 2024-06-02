#Exercise 15.1

import math

# Define a class named Point to represent a point in 2D space
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# Define a class named Circle with attributes center (a Point object) and radius (a number)
class Circle:
    def __init__(self, center=None, radius=0):
        if center is None:
            center = Point()
        self.center = center
        self.radius = radius

# Define a class named Rectangle with attributes corner (a Point object), width, and height
class Rectangle:
    def __init__(self, corner=None, width=0, height=0):
        if corner is None:
            corner = Point()
        self.corner = corner
        self.width = width
        self.height = height

# Function to check if a point is inside or on the boundary of the circle
def point_in_circle(circle, point):
    distance = math.sqrt((point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2)
    return distance <= circle.radius

# Function to check if a rectangle is entirely inside or on the boundary of the circle
def rect_in_circle(circle, rect):
    # Check all corners of the rectangle
    corners = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    # If all corners are inside or on the boundary of the circle, return True
    return all(point_in_circle(circle, corner) for corner in corners)

# Function to check if any corner of the rectangle falls inside the circle
def rect_circle_overlap(circle, rect):
    # Check all corners of the rectangle
    corners = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    # If any corner is inside the circle, return True
    return any(point_in_circle(circle, corner) for corner in corners)

# Instantiate a Circle object with center at (150, 100) and radius 75
center_point = Point(150, 100)
circle = Circle(center_point, 75)

# Example usage
point = Point(160, 110)
rect = Rectangle(Point(100, 50), 50, 30)

print(point_in_circle(circle, point))  # Output: True or False depending on the point
print(rect_in_circle(circle, rect))    # Output: True or False depending on the rectangle
print(rect_circle_overlap(circle, rect))  # Output: True or False depending on the overlap

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle()
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(circle, box.corner))  
    print(rect_in_circle(circle, box))          
    print(rect_circle_overlap(circle, box))     

if __name__ == '__main__':
    main()
