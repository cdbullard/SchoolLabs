def integer_errors(user_list):
    user_list = user_list
    for x in range(5):
        try:
            user_input = int(input("Enter an integer: "))
            user_list.append(user_input)
        except ValueError:
            print("Input value cannot be converted to integer")
            continue
    return user_list


if __name__ == '__main__':
    user_list = []
    print("Integer list: ", integer_errors(user_list))
