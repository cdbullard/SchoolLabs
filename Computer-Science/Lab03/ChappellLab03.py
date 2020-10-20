from random import randint


def int_comparison(int1, int2, int3, int4):
    # init variables
    even_ints = []
    odd_ints = []
    pos_ints = []
    neg_ints = []
    gt_neg25_lt25 = []

    # group integers into an iterable object
    int_list = [int1, int2, int3, int4]
    max_int = max(int_list)
    min_int = min(int_list)
    for integer in int_list:
        if integer %2 == 0:
            even_ints.append(integer)
        else:
            odd_ints.append(integer)
        if -25 < integer < 25:
            gt_neg25_lt25.append(integer)
        else:
            pass
        if integer > 0:
            pos_ints.append(integer)
        elif integer < 0:
            neg_ints.append(integer)
        else:
            pass

    return dict(max_int=max_int, min_int=min_int, gt_neg25_lt25=gt_neg25_lt25, pos_ints=pos_ints,
                odd_ints=odd_ints, even_ints=even_ints, int_list=int_list, neg_ints=neg_ints)


if __name__ == '__main__':
    upper_rand = 50
    lower_rand = -50
    results = int_comparison(randint(lower_rand, upper_rand), randint(lower_rand, upper_rand),
                             randint(lower_rand, upper_rand), randint(lower_rand, upper_rand))

    print(f"The integers are {str(results['int_list']).strip('[]')}")
    print(f"The maximum integer is {results['max_int']}")
    print(f"The minimum integer is {results['min_int']}")
    print(f"The number of even integers is {len(results['even_ints'])}")
    print(f"The number of odd integers is {len(results['odd_ints'])}")
    print(f"The number of integers greater than -25 but less than 25 is {len(results['gt_neg25_lt25'])}")
    print(f"The number of positive integers is {len(results['pos_ints'])}")
    print(f"The number of negatives integers is {len(results['neg_ints'])}")
    print(f"The average of the smaller and largest integers is {results['max_int'] + results['min_int'] / 2}")
    print(f"The average of the four integers is {sum(results['int_list']) / len(results['int_list'])}")
