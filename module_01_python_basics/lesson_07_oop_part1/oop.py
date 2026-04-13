"""
Homework (Lesson 7)
"""


"""1
Rectangle
Create a Rectangle class that takes the width and height of the rectangle upon creation and should have the corresponding attributes width and height (integers).
Create an area() method that returns the area of the rectangle.
Create a perimeter() method that returns the perimeter of the rectangle.
Example:
rect = Rectangle(2, 4)
a = rect.area() # Returns 8
p = rect.perimeter() # Returns 12"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

rect = Rectangle(2, 4)
a = rect.area()
p = rect.perimeter()
print(a)
print(p)


"""2
Car
Create a Car class that takes the car make as a string and the maximum possible speed (max_speed) as an integer upon creation. Also during initialization (in the body of __init__), a speed attribute should be automatically created, equal to 0 (the current speed of the car). Hint: for speed in init you can write self.speed = 0

Create a display_speed() method that prints the current speed of the car to the console.
Create an accelerate() method that increases the car's speed by 10, but the car's speed should not exceed max_speed. If accelerate() is called at maximum speed, the speed should not increase.
Create a brake() method that decreases the car's speed by 10, but the car's speed cannot be less than 0. If the brake() method is called at speed 0, the speed should not decrease.
Example:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # prints 30 to the console"""

class Car:
    def __init__(self, make: str, max_speed: int):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        if self.speed + 10 <= self.max_speed:
            self.speed += 10

    def brake(self):
        if self.speed - 10 >= 0:
            self.speed -= 10
        
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()