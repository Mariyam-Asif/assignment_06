class Car: 
    def __init__(self, brand):
        self.brand = brand # Public Variable
    
    def start(self):
        print(f"{self.brand} car is starting...")
    
my_car = Car("Toyota")

print(my_car.brand)
my_car.start()