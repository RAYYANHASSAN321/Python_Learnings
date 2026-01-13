# #--------------Single if block-------------#


# # username = "admin"
# # password = "adm123"

# # if(username == "admin"):
# #     print("Welcome to the portal")
# #     print("Your role is admin!!")

# # else:
# #     print("wrong email!!")
    


# # age = int(input("Enter your age : "))

# # if(age >= 18):

# #     print("you are eligible for context!")
# #     print("This is if block")
# #     print("We are practicing conditional statement")

# # else:
# #     print("you are not eligible for context!")



# # print("Now you are out of block!!")


# # #------------Else if block -------------------#

# # percetange = int(input("Enter your percentage: "))

# # if percetange >= 80:
# #     print("A+")

# # elif (percetange >= 70):
# #     print("A")

# # elif percetange >= 60:
# #     print("B")

# # elif (percetange >= 50):
# #     print("C")

# # else:
# #     print("Fail")


# # #-----------------Nested if---------------------#

# num = int(input("Enter number : "))

# if(num > 0):

#     if(num % 2 == 0):
#         print(f"{num} is even number")
    
#     else:
#         print(f"{num} is odd number")


# else:
#     print(f"number should be greater than 0")



# #-------------Ternary operator -----------------------#

# age = int(input("Enter age : "))

# status = "Adult" if age >= 18 else "Teenage"

# print(status)

# percent = int(input("Enter percentage : ")) 

# grade = "A+" if percent >= 80 else "A" if percent >= 70 else "B" if percent >= 60 else "Fail"

# print(grade)


#------------------------And Or operator -----------------------------#

# #--------and operator ------------------#

# age = 20
# is_CNIC = False


# if age >= 18 and is_CNIC == True:

#     print("You are eligible for context!!")

# elif age >= 18 and is_CNIC == False:
#     print("Must have CNIC for context!")

# else:
#     print("Age must be greater than 18!!")


# #--------------or operator ----------------

# is_student = True 
# is_ID = False
# is_pass = True


# if is_student == True and (is_ID == True or is_pass == True):
#     print("you are eligible!!")

# else:
#     print("you are not eligible!!")



# #-------------------Match Cases  (switch statement)-----------------------------#

# num = int(input("Enter number less than 10 : "))

# match num:
#     case n if n <= 0:
#         print("Number is 0")
#     case 1 | 2 | 3 | 5 |7:

#         print("Odd Number / Prime number")

#     case n if n % 2 == 0:
#         print("Even Number")
    
#     case _:
#         print("Number is greater than 10")


# #-------------type -----------------------#

# value = [12 , 5 , 6 , 8]

# match value:
#     case int():
#         print(f"Integer value : {value}")
    
#     case str():
#         print(f"String value : {value}")
    
#     case float():
#         print(f"Float value : {value}")
    
#     case _:
#         print(f"unknown type")



#---------------------Loop ------------------------------#

cities = ["Karachi" , "Lahore" , "Quetta" , "Islamabad" , "Hderabad"]


for c in cities:
    print(c)

#-----------------------------#

print("Hello world!")

for i in range(10):
    print("Welcome to Python!!")
    print(i)


#-----------------------------#

for j in range(2 , 8):
    print(j)
#-----------------------------#

for i in range(10):

    if i == 5:
        continue
    print(i)

#-----------------------------#

for i in range(10):

    if i % 2 != 0:
        continue
    print(i)

#-----------------------------#

for i in range(10):

    if i == 5:
        break
    print(i)

#-----------------------------#

nums = [67 , 89 , 34 , 12 , 5 , 23]

for i in nums:
    print(i)
    print("This is nums array data")

else:
    print("Loop is terminated!")

#-----------------------------#

name = "Asad"

print(name.startswith("As"))

#-----------------------------#


names = ["Ahmed" , "Asad" , "Kashif" , "Saad" , "Rehan" , "Raza"]

a = input("Search with : ")

for i in names:

    if(i.startswith(a)):
        print(i)

