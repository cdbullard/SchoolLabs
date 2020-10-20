def vendor_stand(num_hotdogs, num_chips, num_sodas):
    total_due = num_hotdogs * 2.5 + num_chips * 1.5 + num_sodas * 1.25
    return total_due


if __name__ == '__main__':
    num_hotdogs = int(input('Enter number of hotdogs:\n'))
    num_chips = int(input('Enter number of chips:\n'))
    num_sodas = int(input('Enter number of sodas:\n'))
    print(f'The total amount due is ${vendor_stand(num_hotdogs, num_chips, num_sodas)}')
