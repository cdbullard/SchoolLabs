from random import randint
from random import choice as randchoice
from string import ascii_letters
from math import ceil



def binary_search(given_list, target):
    # sort the list
    given_list = sorted(given_list)
    print("current list values", given_list)
    # define starting index
    start = 0
    # define ending index, since index begins at 0, end index is the length of the array - 1
    end = len(given_list) - 1
    # if we have an even numbered list, where start = 0 and end = length of array - 1, we need to round up our index
    # to the nearest integer given length of array 8; start = 0; end = 7; (0 + 7) / 2 == 3.5...can't have a
    # non-integer index, round up using ceiling function
    test_entry = ceil((start + end) / 2)
    print("max possible list index:", len(given_list) - 1)
    print("index position:", test_entry)
    print("value at index", test_entry, "is:", given_list[test_entry])
    if target == given_list[test_entry]:
        print("Found target:", target, "in list")
        return
    elif target < given_list[test_entry]:
        if len(given_list) == 1 and given_list[test_entry] != target:
            print("Target", target, "not in list")
            return
        # set the new ending index to that of the entry checked
        end = test_entry
        # 0 is the default starting index when slicing a list, no need to pass 0:end, :end is acceptable
        sublist = given_list[:end]
        binary_search(sublist, target)
    elif target > given_list[test_entry]:
        if len(given_list) == 1 and given_list[test_entry] != target:
            print("Target", target, "not in list")
            return
        start = test_entry
        # when slicing default end index is -1, and step is defaulted to 1
        # slicing a list --> list[start:end:step] when a slicing argument is empty, the default is used
        sublist = given_list[start::]
        binary_search(sublist, target)


if __name__ == '__main__':
    list1 = [ascii_letters[_].upper() for _ in range(17)]
    print(list1)
    # list1 = [randchoice(ascii_letters) for _ in range(26)]
    binary_search(list1, 'J')
    # list2 = [randint(1, 1000) for _ in range(100)]
    # binary_search(list1, 'J')
    list1.sort()
