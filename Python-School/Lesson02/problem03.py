def aquarium_groups(admission, shark_show, too_much_fun):
    discount_price = (14 + 8) * .75
    total_amount_due = admission * 14 + shark_show * 8 + too_much_fun * discount_price
    return total_amount_due

if __name__ == '__main__':
    admission = int(input('How many group members want just admission:\n'))
    shark_show = int(input('How many group members want just the shark show:\n'))
    too_much_fun = int(input('How many group members want admission and the shark show:\n'))
    print(f'The total amount due for your group is ${aquarium_groups(admission, shark_show, too_much_fun)}')
