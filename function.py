# #---------------Built in function----------------------#

# #----------String functions------------#


text = input("Enter a word : ")

print("Length of text : " , len(text))
print("Upper case : " , text.upper())
print("Lower case : " , text.lower())
print("Capital Case : " , text.capitalize())
print("Check end of text : " , text.endswith("r"))
print("Check start of text : " , text.startswith("a"))


# #----------Numeric functions------------#

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

numbers = [a , b , c]

print("Maximum number : " , max(numbers))
print("Minimum number : " , min(numbers))
print("Sum of number : " , sum(numbers))
print("Average of number : " , sum(numbers) / len(numbers))



#----------------Custom functions------------------#

#---non-paramterized function-----#


def welcome():
    print("Welcome to Python!!")

print("This is message!!!")

# calling function
welcome()

#---Single paramter----#

def greet(name):
    print(f"Welcome {name}")

greet('ali')
greet('saif')


def square(num):
    s = num * num
    print(s)

square(2)
square(6)
square(5)

#-----------------Multi Parameter----------------#

def greet(name , role):
    print(f"Welcome {name} , and your role is : {role}")

greet('ali' , 'admin')


def multiple(num1 , num2):
    print(num1 * num2)

# multiple(4 , 7)



def add (num1 , num2):
    print(num1 + num2)
    return num1 + num2


result = add(3 , 6)

print(result)

answer = multiple(4 , 7)


# print(answer)


def check(num):
    if(num % 2 == 0):
        return True
    else:
        return False
    

n = int(input("Enter number : "))
print(check(n))



#------------------ Palindrome checking ---------------#


# eye
# level 
# madam

def plalindrome_check(word):
    return word == word[:: -1]

print(plalindrome_check("madam"))