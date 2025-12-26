print("Welcome to Python Programming!")

name = "Ahmed" # string 
height = 6.1 # float 

is_CNIC = True # boolean 

print(f"Student name is {name} , height is {height} and CNIC status is {is_CNIC}")


print("student name is : " , name)

print(f"student name is : {name}")


#------------------ OPERATORS --------------#

a = 20 
b = 30

sum = a + b # add
subtract = a - b # subtract
multiply = a * b # multiply 
divide = a / b  # divide
modulas = a % b # modulas
# Exponent = a % b # Exponent
power_of = a ** 2 # power of 


print(f"Sum is : {sum}")
print(f"Subtract is : {subtract}")
print(f"multiply is : {multiply}")
print(f"divide is : {round(divide)}")
print(f"modulas is : {modulas}")
print(f"Subtract is : {subtract}")
# print(f"Exponent is : {Exponent}")
print(f"Power of is : {power_of}")

#-----------------------Assignment operators -----------------------#

a = 12
b = 10
c = 15
d = 45
e = 23

b += a   # Equivalent to b = b + a
c -= b   # Equivalent to c = c - b
d *= a   # Equivalent to d = d * a
e /= c   # Equivalent to e = e / c

print(e)

name = input("Enter your name : ")
num1 = input("Enter your num1 : ")
num2 = input("Enter your num2 : ")

sum = int(num1) + int(num2)

print("name is " , name)
print("sum is : " , sum)

#-----------------------String function ----------------------------#
sum = int(num1) + int(num2)

print("name is " , name)
print("sum is : " , sum)

#-----------------------String function ----------------------------#

name = "Pakistan"

print(len(name))
print(name.endswith("n"))
print(name.startswith("p"))
print(name.capitalize())
print(name.upper())
print(name.lower())

a = name[0:3]
a = name[1]
a = name[-4 : -1]
a = name[ : 6]
a = name[0 : ]
print(a)


