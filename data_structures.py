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