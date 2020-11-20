class Course:
    def __init__(self, course_code, max_class_size):
        self.__enrollment = 0
        self.__course_code = course_code
        self.__max_class_size = max_class_size

    def add_student(self):
        if self.__enrollment < self.__max_class_size:
            self.__enrollment += 1
            print("One student added")
        else:
            print("Course already full")
            print("Course Max Enrollment:", self.__max_class_size, "Current Enrollment:", self.__enrollment)

    def drop_student(self):
        if self.__enrollment > 0:
            self.__enrollment -= 1
            print("One student dropped")
        else:
            print("Course enrollment is empty")

    def get_enrollment(self):
        return self.__enrollment

    def get_max_class_size(self):
        return self.__max_class_size

    def get_course_code(self):
        return self.__course_code

    def set_max_class_size(self, max_class_size):
        self.__max_class_size = max_class_size

    @staticmethod
    def exit_program():
        exit(0)
