class Person:
    def __init__(self, name):
        self.name = name 
        print(f"Person constructor called. Name set to: {self.name}")

# Child class (inherits from Person)
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) # Calls the constructor of Person class
        self.subject = subject
        print(f"Teacher constructor called. Subject set to {self.subject}")

t1 = Teacher("Ms. Sarah", "Mathematics")