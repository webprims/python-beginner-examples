class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        return f"Hi, I am {self.name} and I am learning {self.course}."


student = Student("Gurleen", "Python")
print(student.introduce())
