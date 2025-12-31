# ------------------ Single if block ---------------- #
age = int(input("Enter your age : "))

if(age >= 18):
    print("you are eligible for the context!")
    print("This is if block")
    print("We are practicing conditional statement")
else:
    print("you are not eligible for the context!")

print("now you are ot of block!!")

#--------------- Else if -----------------# 

percentage = int(input("Enter your percentage: "))

if percentage >= 80:
    print("A+")
elif (percentage >= 70):
    print("A")
elif percentage >= 60:
    print("B")
elif (percentage >= 50):
    print("C")
else:
    print("Fail")
    
#-------------------Nested if-----------------------#

num = int(input("Enter number : "))

if(num > 0):
    
    if(num % 2 == 0):
        print(f"{num} is even number")
        
    else:
        print(f"{num} is odd number")

else:
    print(f"number should be greater than 0")


#-------------------Ternary operator -------------------#

age = int(input("Enter age : "))

status = "Adult" if age >= 18 else "Teenage"

print(status)

percent = int(input("Enter percentage : "))

grade = "A+" if percent >= 80 else "A" if percent >= 70 else "B" if percent >= 60 else "Fail"

print(grade)