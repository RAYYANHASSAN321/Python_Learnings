name = input("Enter student name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

cnic_input = input("Do you have CNIC? (yes/no): ").lower()
has_cnic = True if cnic_input == "yes" else False

sub1 = float(input("Enter Subject 1 marks: "))
sub2 = float(input("Enter Subject 2 marks: "))
sub3 = float(input("Enter Subject 3 marks: "))

marks = [sub1, sub2, sub3]

total_marks = sum(marks)
percentage = (total_marks / 300) * 100

print("Name:", name)
print("Age:", age)
print("City:", city)

if has_cnic:
    print("CNIC Status: Verified Student")
else:
    print("CNIC Status: Not Verified Student")

print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")

print("Length of Name:", len(name))

print("First Subject Marks:", marks[0])
print("Last Subject Marks:", marks[-1])
