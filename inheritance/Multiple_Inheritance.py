class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):  
    def show_role(self):
        print(self.name, "is a student")

class ClassRepresentative(Student):
    def assign_section(self, section):
        print(self.name, "is the representative of section", section)



