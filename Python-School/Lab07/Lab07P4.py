def grade_calculator (lab_scores, test_scores, lab_weight=0.5, test_weight=0.5):
    while lab_weight + test_weight != 1:
        print('Lab and Test weights must equal 100')
        lab_weight = int(input('Enter lab percentage as an integer: ')) / 100
        test_weight = int(input('Enter test weight percentage as an integer: ')) / 100
    lab_average = sum(lab_scores) / len(lab_scores)
    test_average = sum(test_scores) / len(test_scores)
    print('Lab average:', lab_average)
    print('Test average:', test_average)
    print('Course grade:', lab_average * lab_weight + test_average * test_weight)
    return


if __name__ == '__main__':
    num_of_labs = int(input('How many labs? '))
    lab_scores = [int(input('Enter a lab score: ')) for x in range(num_of_labs)]
    print('Lab scores are: ', lab_scores)
    num_tests = int(input('How many tests? '))
    test_scores = [int(input('Enter a test score: ')) for x in range(num_tests)]
    print('Test scores are: ', test_scores)
    print('The default weights for course grade are 50% labs and 50% tests.')
    weighted_choice = input('Enter C to change the weights or D to use default weights: ').upper()
    if weighted_choice == 'D':
        grade_calculator(lab_scores, test_scores)
    else:
        grade_calculator(lab_scores=lab_scores, test_scores=test_scores,
                         lab_weight=int(input('Enter lab percentage as an integer: ')) / 100,
                         test_weight=int(input('Enter test weight percentage as an integer: ')) / 100)
