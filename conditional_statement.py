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
    