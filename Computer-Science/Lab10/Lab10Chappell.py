import random
from math import ceil


def fill(nx, x, y):
    # Populate list of size = nx with random integers
    # in the range x  y
    # this code needs to be adjusted does NOT address duplicates
    lx = []
    j = 0
    while j < nx:
        rand_num = random.randint(x, y)
        if rand_num not in lx:
            lx.append(rand_num)
            j = j + 1
    return lx


def display(lx):
    # display 5 lines with each line containing only 5 integers
    index = 0
    length = len(lx)
    print("Prob #2")
    while index < length:
        print("List with 5 integers per line: ", lx[index:(index + 5)])
        index += 5


def sortDescending(lx):
    lx = sorted(lx)
    lx = lx[::-1]
    return lx


def sum(lx):
    # Sum of integers in the list
    s = 0
    for item in lx:
        s += item
    return s


def minValue(lx):
    small = min(lx[::])
    return small

def maxValue(lx):
    mx = max(lx[::])
    return mx


def ave(lx, sum_of_all_fears):
    # returns average of provided list of integers
    average = sum_of_all_fears / len(lx)
    return average


def evens(lx):
    # returns number of even integers in provided list
    e = 0
    for num in lx[::]:
        if num % 2 == 0:
            e += 1
    return e


def odds(lx):
    # returns number of odd numbers in provided list
    o = 0
    for num in lx[::]:
        if num % 2 != 0:
            o += 1
    return o


def digit1x(lx):
    # returns the number of integers in a list that are between 10-19 inclusive
    dig1x = 0
    for num in lx[::]:
        if str(num)[0] == '1':
            dig1x += 1
    return dig1x


def digitx1(lx):
    # returns number of integers in a list that have 1 as the second number
    digx1 = 0
    for num in lx[::]:
        if str(num)[1] == '1':
            digx1 += 1
    return digx1


def div3(lx):
    # returns number of integers that are evenly divisible by 3
    divis_3 = 0
    for num in lx[::]:
        if num % 3 == 0:
            divis_3 += 1
    return divis_3


def median(lx):
    # returns median integer in provided list
    end = len(lx) - 1
    return sorted(lx)[ceil(end / 2)]


def maxMinAverage(minx, maxx):
    # returns average of smallest and largest values from list
    t = (minx + maxx) / 2
    return t


def FirstLast(x, y):
    #  x = return value of minValue()
    #  y = return value of maxValue()
    # create an integer z consisting of the first digit
    # of x and
    # the last digit of y
    z = int(str(x)[0] + str(y)[1])
    return z


def IsFirstLastinMyList(lx, zx):
    # NEEDS to be FIXED
    #  zx = return value of function FirstLast()
    #  if zx in lx let s =‘Yes’
    # other wise s = 'No'
    if zx in lx[::]:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    my_list = fill(25, 10, 60)
    display(my_list)
    reverse_list = sortDescending(my_list)
    print("Problem #3: list in descending order:", reverse_list)
    my_list_sum = sum(my_list)
    print("Problem #4: sum of list:", my_list_sum)
    smallest = minValue(my_list)
    print("Problem #5: smallest value in list:", smallest)
    largest = maxValue(my_list)
    print("Problem #6: max value in list:", largest)
    my_avg = ave(my_list, my_list_sum)
    print("Problem #7: list avg:", my_avg)
    my_evens = evens(my_list)
    print("Problem #8: number of even numbers in list:", my_evens)
    my_odds = odds(my_list)
    print("Problem #9: number of odd numbers in list:", my_odds)
    digits_1x = digit1x(my_list)
    print("Problem #10: number of integers that begin with 1:", digits_1x)
    digits_x1 = digitx1(my_list)
    print("Problem #11: number of integers that have 1 in the second digit:", digits_x1)
    divis_by_3 = div3(my_list)
    print("Problem #12: number of integers evenly divisible by 3:", divis_by_3)
    my_median = median(my_list)
    print("Problem #13: median integer in the list is:", my_median)
    my_max_min_avg = maxMinAverage(smallest, largest)
    print("Problem #14: average of min and max list values is:", my_max_min_avg)
    first_last = FirstLast(smallest, largest)
    print("Problem #15: first digit of smallest number and second digit of largest number:", first_last)
    first_last_in = IsFirstLastinMyList(my_list, first_last)
    print("Problem #16: is answer from #15 in our list?", first_last_in)
