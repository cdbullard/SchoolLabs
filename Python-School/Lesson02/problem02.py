def weighted_grade(lab1, lab2, lab3, test1, test2):
    labs = (lab1 + lab2 + lab3) / 3
    tests = (test1 + test2) / 2
    course_grade = labs * .55 + tests * .45
    return course_grade


if __name__ == '__main__':
    lab1 = int(input('Enter student\'s grade for lab1:\n'))
    lab2 = int(input('Enter student\'s grade for lab2:\n'))
    lab3 = int(input('Enter student\'s grade for lab3:\n'))
    test1 = int(input('Enter student\'s grade for test1:\n'))
    test2 = int(input('Enter student\'s grade for test2:\n'))
    print(f'The students course grade is: {weighted_grade(lab1, lab2, lab3, test1, test2)}')
