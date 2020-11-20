from course import Course


if __name__ == '__main__':
    exit_condition = False
    course_code = input("Enter course code: ").upper()
    max_course_size = None
    while exit_condition is False:
        try:
            max_course_size = int(input("Enter maximum class size: "))
            if max_course_size <= 0:
                raise ValueError
            exit_condition = True
        except ValueError:
            print("Max course size must be a positive integer")
            continue

    my_horse_of_course = Course(course_code=course_code, max_class_size=max_course_size)
    possible_options = (0, 1, 2, 3, 4)
    while True:
        try:
            bandit = int(input("Enter 1 for add student, 2 for drop student, 3 for course info, 4 for "
                               "change maximum class size, 0 for exit: "))
            if bandit not in possible_options:
                raise ValueError
            if bandit == 1:
                my_horse_of_course.add_student()
            elif bandit == 2:
                my_horse_of_course.drop_student()
            elif bandit == 3:
                class_size = my_horse_of_course.get_max_class_size()
                code = my_horse_of_course.get_course_code()
                enrollment = my_horse_of_course.get_enrollment()
                print("Course Code:", code)
                print("Maximum class size:", class_size, "students")
                print("Current Enrollment:", enrollment, "students")
            elif bandit == 4:
                while True:
                    try:
                        new_class_size = int(input("Enter new class size: "))
                        if new_class_size <= 0:
                            raise ValueError
                        elif new_class_size < my_horse_of_course.get_enrollment():
                            print("New maximum class size cannot be lower than current enrollment size")
                            raise ValueError
                        break
                    except ValueError:
                        print("Max course size must be a positive integer and bigger than or equal to enrollment")
                my_horse_of_course.set_max_class_size(new_class_size)
            elif bandit == 0:
                my_horse_of_course.exit_program()
        except ValueError:
            print("Possible choices are:", possible_options)
            continue
