def bill_calculator(customer_type, kwh_used):
    if customer_type.upper() == 'B':
        if kwh_used > 800:
            price = (800 * 0.16) + (kwh_used - 800) * 0.20
            return format(price, '.2f')
        else:
            price = kwh_used * 0.16
            return format(price, '.2f')
    elif customer_type.upper() == 'R':
        if kwh_used > 500:
            price = (500 * 0.12) + (kwh_used - 500) * 0.15
            return format(price, '.2f')
        else:
            price = kwh_used * 0.12
            return format(price, '.2f')


if __name__ == '__main__':
    kwh_used = float(input('Enter kilowatt hours used: '))
    customer_type = input('Enter R for residential customer, B for business customer: ')
    print('Please pay this amount: ', bill_calculator(customer_type=customer_type, kwh_used=kwh_used))
