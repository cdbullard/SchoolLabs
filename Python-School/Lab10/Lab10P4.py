import re


def accounts_billing(customer_type, gallons, account_num):
    charge = 0
    if customer_type == 'R':
        if gallons <= 6000:
            charge = int(gallons) * 0.005
        else:
            charge = 6000 * 0.005 + ((int(gallons) - 6000) * 0.007)
    elif customer_type == 'B':
        if gallons <= 8000:
            charge = int(gallons) * 0.006
        else:
            charge = 8000 * 0.006 + ((int(gallons) - 8000) * 0.008)
    return f"Account number: {account_num}, Water Charge: ${charge:.2f}"


if __name__ == '__main__':
    regex = re.compile("^(\w+) (\w+) (\w+)")
    with open("water.txt", "r") as data:
        for line in data:
            match = regex.search(line)
            if match is not None:
                account_num = match.group(1)
                customer_type = match.group(2)
                gallons = int(match.group(3))
            print(accounts_billing(customer_type, gallons, account_num))
