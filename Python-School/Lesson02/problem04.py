def the_dilemma(jackpot_amount):
    cash_pretax = jackpot_amount * .65
    cash_posttax = cash_pretax * 7
    installment_pretax = jackpot_amount / 20
    installment_posttax = installment_pretax * .7
    print(f'The total instant winnings for the jackpot of ${jackpot_amount} before tax is ${cash_pretax}')
    print(f'The total instant winnings for the jackpot of ${jackpot_amount} after tax is ${cash_posttax}')
    print(f'The annual installment amount for the jackpot of ${jackpot_amount} is ${installment_pretax}')
    print(f'The annual installment amount for the jackpot of ${jackpot_amount} after tax is ${installment_posttax}')
    return

if __name__ == '__main__':
    jackpot_amount = int(input('Please enter the total jackpot amount:\n'))
    the_dilemma(jackpot_amount)
