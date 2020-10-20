def stdin_controller(num_of_scores):
    num_of_scores = num_of_scores
    score = 0
    scores = []
    while 0 < num_of_scores:
        # ensure correct input without raising a program ending error
        try:
            score = int(input("Enter a test score: "))
        except ValueError:
            score = int(input("Please enter a test score as an integer between 0 and 100: "))
        finally:
            while score < 0 or score > 100:
                score = int(input("Please enter a test score as an integer between 0 and 100: "))

        scores.append(score)
        num_of_scores -= 1

    return scores


def test_score_to_list(score_list_in):
    score_list_out = [score if score >= 60 else score + 10 for score in score_list_in]
    score_list_changed = [new_score for (old_score, new_score) in dict(zip(score_list_in, score_list_out)).items()
                          if new_score != old_score]

    return dict(score_list_old=score_list_in, score_list_new=score_list_out, score_list_changed=score_list_changed)


def stdout_controller(score_list_old, score_list_new, score_list_changed):
    print("Original student's scores: ", score_list_old)
    print("Students who scores below 60 get 10 extra points.")
    print("Student's curved scores ", score_list_new)
    print("Student scores that changed: ")
    for score in score_list_changed:
        print(f"Old score: {score - 10}, New score: {score}")

    return


if __name__ == '__main__':
    list_gen = stdin_controller(5)
    score_list = test_score_to_list(score_list_in=list_gen)
    print(score_list)
    stdout_controller(score_list_old=score_list["score_list_old"], score_list_new=score_list["score_list_new"],
                      score_list_changed=score_list["score_list_changed"])




