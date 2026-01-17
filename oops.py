class Employee:
    # Class Attributes
    name = "Ahmed"
    salary = 56000
    designation = "Manager"

    # Constructor
    def __init__(self, con):
        print("Constructor calling")
        self.contact = con

    # Method without parameter
    def info(self):
        print(
            f"Employee name is : {self.name}, "
            f"contact no is : {self.contact}, "
            f"salary is : {self.salary}, "
            f"designation is : {self.designation}"
        )

    def welcome(self):
        print("Welcome to Python")

    # Method with parameters (no return)
    def sum(self, num1, num2):
        print(num1 + num2)

    # Method with return type
    def add(self, num1, num2):
        return num1 + num2


# -------- Object Creation (OUTSIDE class) --------
emp1 = Employee("03128364837248")
emp1.welcome()
emp1.info()

emp2 = Employee("03001234567")
emp2.info()
