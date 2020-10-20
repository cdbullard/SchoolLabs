from random import randint


def theoretical_calc(length, probability, times):
    theory_mean = length * probability * times
    theory_variance = length * times * probability * (1 - probability)
    std_dev = (length * times) ** 0.5
    return dict(theory_mean=theory_mean, theory_variance=theory_variance, std_dev=std_dev)


def binomial_list_generator(random_int_min, random_int_max, length, times):
    binomial_list = [[randint(random_int_min, random_int_max) for x in range(length)] for y in range(times)]
    return binomial_list


def output_loop(binomial_list, theory):
    master_list = [inner_ints for lists in binomial_list for inner_ints in lists]
    mean = sum(master_list) / len(master_list)
    ones = [one for one in master_list if one == 1]
    zeroes = [zero for zero in master_list if zero == 0]
    print('~~~~~ Begin Theoretical Results ~~~~~\n')
    print(f'1: Theoretical mean of 1\'s (n*nn*p) == {theory["theory_mean"]}')
    print(f'2: Theoretical variance v == {theory["theory_variance"]}')
    print(f'3: The standard deviation SD (should be > 100) == {theory["std_dev"]}')
    print('\n~~~~~ End Theoretical Results ~~~~~\n')
    print('~~~~~ Begin Experiment Results ~~~~~\n')
    print('~~~~~ Populate a binomial list and count 1s ~~~~~')
    print(f'4: The length of the generated list is...'
          f'{len(master_list)}')
    print(f'5: The number of 1\'s is: {len(ones)}')
    print(f'6: The number of 0\'s is: {len(zeroes)}')
    print(f'7: The average of all 50,000 integers is...{mean:.3f}')
    print(f'8: The Theoretical mean - 2*SD == {(theory["theory_mean"] - theory["std_dev"]):.3f}')
    print(f'9: The Theoretical mean + 2*SD == {(theory["theory_mean"] + theory["std_dev"]):.3f}')
    if int(theory["theory_mean"] - theory["std_dev"]) <= len(ones) <= int(theory["theory_mean"] + theory["std_dev"]):
        print('10: Is the number of 1\'s within avg +- 2*SD...YES')
    else:
        print('10: Is the number of 1\'s within avg +- 2*SD...NO')
    print('11: Displaying 10 numbered lines with 25 integers per line...')
    x = 1
    for i in range(10):
        print(f'Line {x}: {[int_list for int_list in binomial_list[i][::2]]}')
        x += 1
    print('~~~~~ End Experiment Results ~~~~~')
    return


if __name__ == '__main__':
    output_loop(binomial_list_generator(random_int_min=0, random_int_max=1, length=50, times=1000),
                theoretical_calc(length=50, probability=0.5, times=1000))
