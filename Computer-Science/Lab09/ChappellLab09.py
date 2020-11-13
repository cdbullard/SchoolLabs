if __name__ == '__main__':
    user_input = input("Please enter a string: ")
    d = {i: character for i, character in enumerate(user_input, 0)}
    print("Problem #1:", d)
    print("Problem #2 - Length of Dictionary is:", len(d))
# Problem 3
    while True:
        try:
            user_key = int(input("Please enter a dictionary key to display it's corresponding value: "))
            value = d[user_key]
            print(f"Problem # 3 - The value of {user_key} in dictionary is: {value}")
            break
        except KeyError:
            print("Error, key not found. Try again")
            continue
        except ValueError:
            print("Invalid input, try again")
            continue

    user_value = input("Please enter a value to check it's appearance in dictionary: ")
    if user_value in d.values():
        print("Problem #4: Value found")
    else:
        print("Problem #4: Value not found")

    add_character = input("Please enter a character to add to the dictionary: ")
    d[len(d)] = add_character
    print("Problem #5", d)
    d[(len(d) - 1)] = "Chappell"
    print("Problem #6", d)
# Problem 7
    while True:
        try:
            user_deletion = int(input("Please enter a dictionary key to delete the key value pair: "))
            if user_deletion in d.keys():
                del d[user_deletion]
                print("Problem #7 - dictionary after removing key:", d)
            else:
                print("Problem #7: Key not found")

            break
        except ValueError:
            print("Invalid input, try again")
            continue
# problem 8
    while True:
        try:
            user_digits = input("Please enter a string of digits, separated by commas")
            user_digits = user_digits.split(",")
            out_list = []
            for n in user_digits[::]:
                out_list.append(int(n))
            out_string = ""
            for i in out_list:
                if i in d.keys():
                    out_string += d[i]
                else:
                    out_string += "*"
            print("Problem #8:", out_string)
            break
        except ValueError:
            print("Invalid input, must enter integers")
            continue
