from abc import ABC, abstractmethod

# Abstract base class 
class Shape(ABC): # Shape inherits from ABC

    @abstractmethod
    def area(self):
        pass # This is just a placeholder, child class must implement this

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
# This will give an error
# shape = Shape() # Cannot instantiate abstract class

rect = Rectangle(4, 5)
print("Area of rectangle:", rect.area())