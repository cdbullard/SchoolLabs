def integer_functions(integer_list):

    int_list = integer_list
    list_sum = sum(int_list)
    list_max = max(int_list)
    list_min = min(int_list)
    list_len = len(int_list)
    list_avg = list_sum / list_len
    list_rev = int_list[::-1]
    last_elem_first = integer_list[::1]
    last_elem_first.insert(0, last_elem_first.pop(-1))

    return dict(list_sum=list_sum, list_max=list_max, list_min=list_min, list_len=list_len, list_avg=list_avg,
                list_rev=list_rev, last_elem_first=last_elem_first, list_start=integer_list)


if __name__ == '__main__':
    chicken_wing = "Y"
    integer_list = []

    while chicken_wing.upper() == "Y":
        try:
            new_int = int(input("Enter an integer from 1 to 10: "))
        except ValueError:
            new_int = int(input("PLEASE, there, I said please. Enter an integer from 1 to 10: "))
        while new_int < 1 or new_int > 10:
            new_int = int(input("Please enter an integer between 1 and 10: "))
        integer_list.append(new_int)
        chicken_wing = input("Enter another integer? [y/n]: ")
        while chicken_wing.upper() not in ("Y", "N"):
            chicken_wing = input("Please enter either [y/n] ")

    da_func = integer_functions(integer_list)
    print("Number list: ", da_func["list_start"])
    print("Largest element: ", da_func["list_max"])
    print("Smallest element: ", da_func["list_min"])
    print("Sum of all fears, err, I mean elements is: ", da_func["list_sum"])
    print("Length of list: ", da_func["list_len"])
    print("Average of integers entered: ", da_func["list_avg"])
    print("List reversed: ", da_func["list_rev"])
    print("Last element moved to the front: ", da_func["last_elem_first"])