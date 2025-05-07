class Countdown:
    def __init__(self, start):
        self.current = start # Start counting from this number
    
    def __iter__(self):
        return self # makes the object itself the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration # Stop when we reach below 0 
        else:
            num = self.current # Store the current number
            self.current -= 1 # Count down
            return num # Return the current number
    
countdown = Countdown(7)
for number in countdown:
    print(number)