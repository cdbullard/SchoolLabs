team_a_score = 0
team_b_score = 0

for quarter in range(1,5):
    team_a_score = int(input(f"Enter team A score for quarter {quarter}: ")) + team_a_score
    team_b_score = int(input(f"Enter team b score for quarter {quarter}: ")) + team_b_score
    print(f"The score after quarter {quarter} is \nTeam A: ", team_a_score, "\nTeam B: ", team_b_score)

if team_a_score > team_b_score:
    print("Team A has won")
elif team_b_score > team_a_score:
    print("Team B has won")
elif team_a_score == team_b_score:
    print("It is a tie")