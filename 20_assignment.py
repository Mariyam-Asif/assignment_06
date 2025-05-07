# Custom exception class
class InvalidAgeError(Exception):
    pass

# Function that checks the age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.") # Raise the custom error
    else:
        print("Access granted!")

# try-except to handle the error
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught: ", e)
except ValueError:
    print("Please enter a valid number.")