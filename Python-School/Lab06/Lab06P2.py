# reduce, reuse, recycle, rihanna
def stdin_controller (num_of_scores):
    num_of_scores = num_of_scores
    score = 0
    scores = []
    while 0 < num_of_scores:
        # ensure correct input without raising a program ending error
        try:
            score = float(input("Enter a score: "))
        except ValueError:
            score = float(input("Please enter a score as a number between 0 and 100: "))
        finally:
            while score < 0 or score > 100:
                score = float(input("Please enter a score as a number between 0 and 100: "))

        scores.append(score)
        num_of_scores -= 1

    return scores


if __name__ == '__main__':
    players = ["Jean", "Kayla", "Connie"]

    player_scores = {}
    for player in players:
        print(f'Please enter {player}\'s scores one by one.')
        player_scores[player] = stdin_controller(4)
        print(f'{player}\'s scores: {player_scores[player]}')
        print("\n")
    # Had to actually start paying attention to the Lab instruction here >.< I almost got myself again!

    # I googled for a bit and didn't come up with much.  Curious if it's possible to assign these variable names dynamically
    # for player in players:
    #     player[0]_list = [<csv>]
    #     in first iteration of loop where player is "Jean", the variable name would become j_list

    j_list = player_scores["Jean"]
    k_list = player_scores["Kayla"]
    c_list = player_scores["Connie"]

    all_scores = [j_list[:], k_list[:], c_list[:]]
    print(f'All scores: {all_scores}')
    # all scores plus 1
    asp1 = [[score + 1 for score in player_list] for player_list in all_scores]
    print(f"All scores after extra point: {asp1}")
    as_sorted = [sorted([score for score in player_list]) for player_list in asp1]
    print(f"All scores after sorting: {as_sorted}")






