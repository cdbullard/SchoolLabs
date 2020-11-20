class Course:
    def __init__(self, course_code, max_class_size):
        self.enrollment = 0
        self.course_code = course_code
        self.max_class_size = max_class_size

    def add_student(self):
        if self.enrollment < self.max_class_size:
            self.enrollment += 1
            print("One student added")
        else:
            print("Course already full")
            print("Course Max Enrollment:", self.max_class_size, "Current Enrollment:", self.enrollment)

    def drop_student(self):
        if self.enrollment > 0:
            self.enrollment -= 1
            print("One student dropped")
        else:
            print("Course enrollment is empty")

    def course_info(self):
        print("Course Code:", self.course_code)
        print("Maximum class size:", self.max_class_size)
        print("Enrollment:", self.enrollment)

    @staticmethod
    def exit_program():
        exit(0)
