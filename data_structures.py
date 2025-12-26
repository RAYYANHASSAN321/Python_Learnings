#----------------------------- LIST ----------------------------#
# Mutable and can have duplicate values 

student = ["Ali" , 17 , "Karachi" , 5.6 , False]
print(student)
print(student[0])
student[0] = "Ahsan"

print(student[0])
print(student)
print(student[0 : 3]) # 0 is index and 3 is length

student.append("Python") # append will add after last index 

print(student)

student.insert(2 , "Python") # to add on specified index

print(student)

student.pop(4) # to remove data from specified index
print(student)

student.reverse()
print(student)

marks = [45 , 78 , 95 , 67 , 85 , 83 , 46]
marks.sort()

print(marks)

# -------------------- Tuple --------------------
# immutable and can have duplicate values

employee = ("Ahmed" , "Lahore" , 45000 , "Manager" )

print(employee)
print(type(employee))
print(employee.index(45000))

print(employee[0])
print(employee[-1])  #last element
print(employee[1:3]) # slicing

# count shows how many times the data appeared in tuple
print(employee.count(45000))

# unpacking of data in tuple data structure

name , address , salary , designation  = employee
print(name)
print(address)
print(designation)
print(salary)