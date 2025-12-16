class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is a teacher.")

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def course_info(self):
        print(f"Course assigned:{self.course_name}")

class DepartmentHead(Teacher, Course):
    def __init__(self, name, course_name, department):
        super().__init__(name)
        Course.__init__(self, course_name)
        self.department = department

    def lead_department(self):
        print(f"{self.name} is heading to the {self.department} and going to teach {self.course_name} in BSIS-2B")

