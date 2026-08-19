class Person:
    # This is the constructor
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Student inherits from Person
class Student(Person):
    # This is the constructor for the child class
    def __init__(self, fname, lname, year):
        # Calling the parent constructor
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Usage example:
x = Student("Deepak", "Thorat", 2027)
x.welcome()
