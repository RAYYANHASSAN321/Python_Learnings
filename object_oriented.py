class Employee:
    #
    name = "Adnan"
    salary = 67000
    designation = "Manager"
    
    #method without parameter
    
    def welcome(self):
        print("Welcome to object oriented programming")
    
    def msg(self , name):
        self.age = 34
        email = "adnan@email.com"
        print(f"Welcome {name} , your age is {self.age} , email is {email}")
    
    def details(self):
        print(f"Your salary is : {self.salary} , and your age is : {self.age}")
        
emp = Employee() # Instance / object of class
print(emp.name)

emp.welcome()
emp.msg("Asad")
emp.details()