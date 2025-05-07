# Define the decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func() # Call the original function
    return wrapper # Reture the wrapped function

# Define a function to be decorated
@log_function_call
def say_hello():
    print("Hello!")

say_hello() # Call the decorated function