def get_kwh_used():
    try:
        user_input = int(input('Enter kilowatt hours used: '))
        while user_input < 0:  # stay positive - test negative!
            user_input = int(input('Please enter kilowatt hours used as a positive integer: '))
    except ValueError:
        user_input = int(input('Please enter kilowatt hours used as a positive integer: '))
        while user_input < 0:  # stay positive - test negative!
            user_input = int(input('Please enter kilowatt hours used as a positive integer: '))

    return user_input


def bill_calculator(kwh_used):
    if kwh_used <= 500:
        total_bill = kwh_used * 0.12
        return format(total_bill, '.2f')
    elif kwh_used > 500:
        total_bill = (500 * 0.12) + ((kwh_used - 500) * 0.15)
        return format(total_bill, '.2f')


if __name__ == '__main__':
    print(f'Please pay this amount: ${bill_calculator(get_kwh_used())}')
