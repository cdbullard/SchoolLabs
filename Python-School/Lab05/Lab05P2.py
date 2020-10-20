def add_drop(course, course_list, selection):
    course = course
    new_course_list = course_list
    if selection == "A":
        if course in new_course_list:
            print("You are already registered in that course")
            return course_list
        else:
            new_course_list.append(course)
            new_course_list.sort()
            print("Course added")
            print("Courses Registered: ", new_course_list)

    elif selection == "D":
        if course not in course_list:
            print("You cannot drop a class you're not registered for")
        else:
            new_course_list.remove(course)
            new_course_list.sort()
            print("Course dropped")
            print("Courses registered: ", new_course_list)

    return new_course_list


# function to validate user operations
def logic_control(selection, course_list):
    # Force input of either "A", "D", or "E"
    while selection not in ("A", "D", "E"):
        selection = input("Enter A to add course, D to drop course, and E to exit: ")
    # Once input is validated, proceed with program
    if selection == "A":
        return selection
    elif selection == "D":
        # Can't drop a class if you're not registered!
        if len(course_list) == 0:
            print("You are not registered for any courses, you cannot drop a class")
        return selection
    elif selection.upper() == "E":
        return selection


if __name__ == '__main__':
    program_status = ""
    course_list = []
    course = ""
    while program_status != "E":
        program_status = logic_control(
            selection=input("Enter A to add course, D to drop course, and E to exit: ").upper(),
            course_list=course_list)
        if program_status == "E":
            print("Okay, Baaaaaiiiii! \nYou are registered for ", course_list)

            break
        course_list = add_drop(course=input("Enter course to add: ").upper(), course_list=course_list,
                               selection=program_status)
