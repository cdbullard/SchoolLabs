def list_courses (id, c_list, r_list):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------

    cnt = 0
    courses = ""

    for x in range(len(r_list)):
        for y in range(len(r_list[x])):
            if r_list[x][y] == id:
                cnt += 1
                courses += "\n{}".format(c_list[x])

    print("Courses registered:", courses)
    print("Total number:", cnt)


def add_course(id, c_list, r_list, m_list):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    index = 0
    course = input("Enter the course number you wish to add: ").upper()

    if course not in c_list:
        print("Course not found")
        return

    while course != c_list[index]:
        index += 1

    if course == c_list[index] and len(r_list[index]) < int(m_list[index]):
        if id in r_list[index]:
            print("You are already enrolled in that course")
        else:
            r_list[index].append(id)
            print(f"Course {course} added")
    else:
        print("Course already full")


def drop_course(id, c_list, r_list):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    course = input("Enter the course number you wish to drop: ").upper()

    if course not in c_list:
        print("Course not found.")
    else:
        if course == 'CSC101':
            if id in r_list[0]:
                r_list[0].remove(id)
                print("Course dropped.")
            else:
                print("You are not enrolled in that course.")
        elif course == 'CSC102':
            if id in r_list[1]:
                r_list[1].remove(id)
                print("Course dropped.")
            else:
                print("You are not enrolled in that course.")
        elif course == 'CSC103':
            if id in r_list[2]:
                r_list[2].remove(id)
                print("Course dropped.")
            else:
                print("You are not enrolled in that course.")

