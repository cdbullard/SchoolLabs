from random import randint


computer_int = randint(6, 9)
count = 0
print("Computer\'s pick: ", computer_int)

for integer in range(0,3):
    player_int = randint(1, 10)
    print("Your pick: ", player_int)
    if player_int > computer_int:
        print("You have won the game!")
        break
    else:
        count += 1
    if player_int <= computer_int and count == 3:
        print("Sorry, you have lost the game")
