# Class decorator
def add_greeting(cls):

    def greet(self):
        return f"Hello {self.name} from Decorator!"
    
    cls.greet = greet # Add the greet method to the class
    return cls # Return the modified class

# Define the Person class and apply the decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# An object of the Person class
person = Person("Alice")
# Call the greet method added by the decorator
print(person.greet())