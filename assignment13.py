class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower} HP Started"

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower) # Creating Engine object inside Car

    def start_car(self):
        print(f"Starting car model: {self.model}")
        print(self.engine.start()) # Using Engine's method inside Car

# Creating a Car object with model and horsepower
my_car = Car("Toyota Corolla", 150)

my_car.start_car()



        