class Logger:
    # Constructor
    def __init__(self):
        print("Logger started: Object have been created.")
    # Destructor
    def __del__(self):
        print("Logger ended: Object has been destroyed.")

# Create an object of Logger
log = Logger()

# Delete the object manually (just to show destructor)]
del log