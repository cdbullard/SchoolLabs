if __name__ == '__main__':

    currency_types = {
        1: {
            'currency_type': 'Euro',
            'currency_sym': '\u20AC'
        },
        2: {
            'currency_type': 'Japanese Yen',
            'currency_sym': '\u00a5'
        },
        3: {
            'currency_type': 'Mexican Peso',
            'currency_sym': '\u20B1'
        }
    }

    print('Converting US Dollars to foreign currency.')

    try:

        dollars = float(input('Enter amount of US Dollars: '))

        while dollars < 0:
            print('Error: US dollars cannot be negative')
            dollars = float(input('Enter amount of US Dollars: '))

        currency_type = input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: ')

        while int(currency_type) not in currency_types.keys():
            print('Error: Invalid Choice')
            currency_type = input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: ')

    except ValueError:

        print('Dollars cannot be negative')

        dollars = float(input('Enter amount of US Dollars: '))

        while dollars < 0:
            print('Error: US dollars cannot be negative')
            dollars = float(input('Enter amount of US Dollars: '))

        currency_type = input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: ')

        # check currency input against entries in the currency types dictionary
        while int(currency_type) not in currency_types.keys():
            print('Error: Invalid Choice')
            currency_type = input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: ')

# import only the necessary function
    if currency_types[int(currency_type)]['currency_type'] == 'Euro':
        from currency import to_euro as currency
    elif currency_types[int(currency_type)]['currency_type'] == 'Japanese Yen':
        from currency import to_yen as currency
    elif currency_types[int(currency_type)]['currency_type'] == 'Mexican Peso':
        from currency import to_yen as currency

    print(f'${dollars} converted to {currency_types[int(currency_type)]["currency_sym"]}{currency(dollars)} '
          f'{currency_types[int(currency_type)]["currency_type"]}')


