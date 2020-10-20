def bill_calculator(kwh_used):
    kwh_lte_500 = 0.12
    kwh_gt_500 = 0.15
    price = 0
    if kwh_used > 500:
        price = (kwh_lte_500 * 500) + (kwh_used - 500) * kwh_gt_500
        return price
    else:
        price = kwh_used * kwh_lte_500
        return price


if __name__ == '__main__':
    print('Please pay this amount:', format(bill_calculator(int(input('Enter kilowatt hours used: '))), '.2f'))
