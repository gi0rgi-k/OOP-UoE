#Exercise 15.2

import turtle
import math

# Define the Point class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# Define the Circle class
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# Define the Rectangle class
class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

# Function to draw a rectangle using Turtle
def draw_rect(t, rect):
    t.penup()
    t.goto(rect.corner.x, rect.corner.y)
    t.pendown()
    for _ in range(2):
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)

# Function to draw a circle using Turtle
def draw_circle(t, circ):
    t.penup()
    t.goto(circ.center.x, circ.center.y - circ.radius)
    t.pendown()
    t.circle(circ.radius)

# Example usage
def main():
    # Create a Turtle object
    t = turtle.Turtle()

    # Instantiate a Rectangle object
    rect = Rectangle(Point(-50, -50), 100, 200)

    # Instantiate a Circle object
    circ = Circle(Point(100, 100), 75)

    # Draw the rectangle
    draw_rect(t, rect)

    # Draw the circle
    draw_circle(t, circ)

    # Hide the turtle and display 
    t.hideturtle()
    turtle.done()

if __name__ == '__main__':
    main()

