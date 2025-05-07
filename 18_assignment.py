class Product:
    def __init__(self, price):
        self._price = price # Private variable, by convention not strict

    # Getter method to get the price
    @property
    def price(self):
        print("Getting price...")
        return self._price
    
    # Setter method to update the price
    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)

# Access the price
print(p.price)

# Update the price
p.price = 200

# Acess again
print(p.price)

# Delete the price
del p.price