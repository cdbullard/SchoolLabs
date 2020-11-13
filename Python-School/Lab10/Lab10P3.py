from time import sleep


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


def get_account_number():
    try:
        user_input = int(input('account number: '))
        while user_input < 0:
            user_input = int(input('Please enter account number: '))
        customer_type = input('Enter R for residential customer, B for business customer: ').upper()
        while customer_type not in ('R', 'B'):
            print('Invalid customer type')
            customer_type = input('Enter R for residential customer, B for business customer: ').upper()
        gallons_used = int(input('Please enter number of gallons used: '))
        while gallons_used < 0:
            gallons_used = int(input('Please enter number of gallons used: '))
    except ValueError:
        user_input = int(input('Please enter account number as a positive integer: '))
        while user_input < 0:  # stay positive - test negative!
            user_input = int(input('Please enter account number as a positive integer: '))
        customer_type = input('Enter R for residential customer, B for business customer: ').upper()
        while customer_type not in ('R', 'B'):
            print('Invalid customer type')
            customer_type = input('Enter R for residential customer, B for business customer: ').upper()
        gallons_used = int(input('Please enter number of gallons used: '))
        while gallons_used < 0:
            gallons_used = int(input('Please enter number of gallons used: '))

    return str(user_input), str(customer_type), str(gallons_used)


if __name__ == '__main__':
    print("Program will execute until Keyboard Interrupt Signal is received (Ctrl + C)")

    try:
        text_list = []
        while True:

            text_list.append(str(get_account_number()).strip('()').replace(',', '').replace("'", ""))
            with open(file="water.txt", mode="w+") as file:
                for text in text_list:
                    file.write(text + "\n")
            print("[Ctrl + C] now to exit program, if no more accounts")
            sleep(3)
    except KeyboardInterrupt:
        print("\n\nExiting...")
    finally:
        print("Cleaning up...")
        if file:
            file.close()
