'''
Date 12-10-2021

In this tutorial, you will learn about Abstract base Class
Note: If you use Abstract base Class with function declared with method "@abstractmethod" then that function must be declared in further derived class
'''

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_area(self):
        print(
            f"Are of rectangle with width {self.width}cm and height {self.height}cm is {self.height*self.width}")


rect = Rectangle(8, 9)
rect.print_area()
