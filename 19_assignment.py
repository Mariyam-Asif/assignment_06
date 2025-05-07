class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number): # This lets the object be called like a function
        return number * self.factor

multiply = Multiplier(5) # Create an object of Multiplier
print(multiply(20)) # Test the object like a function
print(callable(multiply)) # Check if the object is callable