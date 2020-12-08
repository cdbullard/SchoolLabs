# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

import student


def main():

    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]

    id = 0
    selection = 4

    while True:
            id = input("Please enter your student ID, or 0 to quit: ")
            if int(id) == 0:
                break
            elif id not in (element for sublist in student_list for element in sublist):
                while id not in (element for sublist in student_list for element in sublist):
                    print("Student ID incorrect, please enter your student number")
                    id = input("Please enter your student ID, or 0 to quit: ")
                    if id in (element for sublist in student_list for element in sublist):
                        login(id, student_list)
            elif id in (element for sublist in student_list for element in sublist):
                login(id, student_list)

            while selection != 0:
                try:
                    selection = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                    if selection == 1:
                        student.add_course(id=id, c_list=course_list, r_list=roster_list, m_list=max_size_list)
                    elif selection == 2:
                        student.drop_course(id=id, c_list=course_list, r_list=roster_list)
                    elif selection == 3:
                        student.list_courses(id=id, c_list=course_list, r_list=roster_list)
                    elif selection == 0:
                        break

                except ValueError:
                    print("Invalid entry, please try again.")


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    index = 0
    while id != s_list[index][0]:
        index += 1
    student_pin = input("Enter student PIN: ")
    if student_pin == s_list[index][1]:
        print("ID and PIN verified")
        return True
    else:
        count = 0
        while count < 3 and student_pin != s_list[index][1]:
            print(f"Incorrect Student PIN, you have {3 - count} attempts left")
            student_pin = input("Enter student PIN: ")
            count += 1

        if count == 3:
            return False
        else:
            print("ID and PIN verified")
            return True

main()
