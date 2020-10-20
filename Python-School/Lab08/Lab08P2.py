def get_kwh_used():
    try:
        user_input = int(input('Enter kilowatt hours used: '))
        while user_input < 0:  # stay positive - test negative!
            user_input = int(input('Please enter kilowatt hours used as a positive integer: '))
        customer_type = input('Enter R for residential customer, B for business customer: ').upper()

        while customer_type not in ('R', 'B'):
            print('Invalid customer type')
            customer_type = input('Enter R for residential customer, B for business customer: ').upper()
    except ValueError:
        user_input = int(input('Please enter kilowatt hours used as a positive integer: '))
        while user_input < 0:  # stay positive - test negative!
            user_input = int(input('Please enter kilowatt hours used as a positive integer: '))
        customer_type = input('Enter R for residential customer, B for business customer: ').upper()
        while customer_type not in ('R', 'B'):
            print('Invalid customer type')
            customer_type = input('Enter R for residential customer, B for business customer: ').upper()

    return dict(kwh_used=user_input, customer_type=customer_type)


def bill_calculator(kwh_used, customer_type):
    total_bill = 0
    if customer_type == 'R':
        if kwh_used <= 500:
            total_bill = kwh_used * 0.12
        elif kwh_used > 500:
            total_bill = 500 * 0.12 + (kwh_used - 500) * 0.16
        return format(total_bill, '.2f')
    elif customer_type == 'B':
        if kwh_used <= 800:
            total_bill = kwh_used * 0.16
        elif kwh_used > 800:
            total_bill = 800 * 0.16 + (kwh_used - 500) * 0.2
        return format(total_bill, '.2f')


if __name__ == '__main__':
    user_data = get_kwh_used()
    print(f'Please pay this amount: ${bill_calculator(user_data["kwh_used"], user_data["customer_type"])}')
