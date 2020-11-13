from random import randint


if __name__ == '__main__':
    set1 = {randint(1, 10) for x in range(5)}
    set2 = {randint(1, 10) for x in range(5)}
    union = set1 | set2
    odds = {x for x in union if x % 2 != 0}
    intersection = set1 & set2
    symmetry = set1 ^ set2
    print("Set1:", set1)
    print("Set2:", set2)
    print("Union of set1 and set2:", union)
    print("Odd numbers in union of set1 and set2:", odds)
    print("Symmetric difference of set1 and set2:", symmetry)
