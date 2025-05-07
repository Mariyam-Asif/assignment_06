class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # Public 
        self._salary = salary # Protected
        self.__ssn = ssn # Private

# Creating an object of Employee
emp = Employee("Amna", 50000, "123-45-6789")

# Try Accessing all the variables
print("Public:", emp.name) # works
print("Protected:", emp._salary) # works but should be treated as "internal use only"
print("Private:", emp.__ssn) # Error! Can't access directly