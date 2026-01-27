class Student:
    def __init__(self, name):
        self._name = name       
        self.__marks = None    

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


class GraduateStudent(Student):
    def grade(self):
        marks = self.get_marks()
        if marks >= 80:
            return "A"
        elif 60 <= marks <= 79:
            return "B"
        else:
            return "C"


student = GraduateStudent("Rayyan Hassan")
student.set_marks(85)

print("Student Name:", student._name)
print("Marks:", student.get_marks())
print("Grade:", student.grade())
